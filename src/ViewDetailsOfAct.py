import Util

drama = []

def menu(temp_drama):
    global drama
    success = Util.validate_drama(temp_drama)
    if success:
        drama = temp_drama
        get_act_from_drama()


def get_act_from_drama():
    global drama
    print("Please enter the act number:")
    selection = input()
    if selection.isdigit():
        selection = int(selection)
        if selection <= Util.find_number_of_acts(drama):
            print("Act " + str(selection) + " details:")
            for line in drama:
                if line.startswith("ACT " + Util.convert_int_to_numerals(selection)):
                    pass
            words, lines, character_names_and_utterances = count_utterance_words_in_act(selection)
            print("Number of spoken words in act : " + str(words))
            print("Number of spoken lines in act : " + str(lines))
            print("\n")
            print("Character who speaks the most: " + str(max(character_names_and_utterances, key=character_names_and_utterances.get)))
            print("Character who speaks the least: " + str(min(character_names_and_utterances, key=character_names_and_utterances.get)))
            print("\n")
            print("Scene names:")
            scenes = get_scene_names(selection)
            if scenes is not None:
                for scene in scenes:
                    print(scene)
            else:
                print("No scenes found.")
            print("\n")
        else:
            print("Invalid act number " + str(selection))

def extract_between_acts(start_act):
    global drama
    start_idx, end_idx = Util.get_act_bounds(start_act, drama)
    if start_idx is None:
        return []
    #if end_act is specified, adjust end_idx accordingly
    return drama[start_idx:end_idx]

def match_speaker(line, char_patterns):
    up = line.upper()
    for pat in char_patterns:
        if up.startswith(pat):
            next_idx = len(pat)
            #check that the next character is a valid separator
            if next_idx == len(up) or up[next_idx] in ".: \t":
                #return the speaker pattern and the remainder of the line
                remainder = line[next_idx:].lstrip(".: \t")
                return pat, remainder
    return None, None


def count_utterance_words_in_act(act_number):
    global drama
    characters = Util.get_character_names(drama)
    utterances = extract_between_acts(act_number)
    if not utterances or not characters:
        return 0, 0, {}

    #sort character names longest to shortest, so that we can match longest names first
    char_patterns = sorted((c.upper().strip() for c in characters if c.strip()), key=len, reverse=True)

    current_speaker = None
    words = 0
    lines = 0
    character_names_and_utterances = {}

    for raw in utterances:
        line = raw.strip()
        if not line:
            continue

        #skip ACT and SCENE headers
        if line.startswith("ACT ") or line.startswith("SCENE ") or line.startswith("Scene "):
            current_speaker = None
            continue

        #skip stage directions in square brackets
        if line.startswith("["):
            current_speaker = None
            continue

        #skip Enter/Exit stage directions (but not if inside dialogue)
        if line.startswith("Enter ") or line.startswith(" Enter") or line.startswith("_Exit"):
            current_speaker = None
            continue

        #check for speaker
        speaker, remainder = match_speaker(line, char_patterns)
        if speaker:
            if speaker not in character_names_and_utterances:
                character_names_and_utterances[speaker] = 0
            current_speaker = speaker
            # if there's dialogue on the same line as the speaker name
            if remainder:
                character_names_and_utterances[current_speaker] += 1
                lines += 1
                words += len(remainder.split())
            continue

        #if we have a current speaker, this is a continuation line
        if current_speaker:
            character_names_and_utterances[current_speaker] += 1
            lines += 1
            words += len(line.split())

    return words, lines, character_names_and_utterances

def get_scene_names(act_number):
    global drama
    scenes = []
    start_idx, end_idx = Util.get_act_bounds(act_number, drama)
    if start_idx is None:
        return []
    for i in range(start_idx, end_idx):
        line = drama[i].strip()
        if line.startswith("SCENE "):
            scenes.append(line.split("SCENE ", 1)[1].strip())
    return scenes