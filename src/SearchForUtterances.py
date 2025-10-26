import Util
import re as re

drama = []
scene_count = 0
act_count = 0

def menu(drama_temp):
    global drama
    success = Util.validate_drama(drama_temp)
    if success:
        drama = drama_temp
        if prompt_for_scene_and_act():
            search_for_words_or_phrases()
            search_first_and_last_utterance()
        else:
            print("Please enter valid scene and act numbers.")
    else:
        print("Please enter a valid scene and act number.")

def prompt_for_scene_and_act():
    global scene_count, act_count
    scene_temp = input("Enter scene number: ")
    act_temp = input("Enter act number: ")
    if scene_temp.isdigit() and act_temp.isdigit():
        scene_temp = int(scene_temp)
        act_temp = int(act_temp)
        #check if act and scene are valid
        if act_temp <= Util.find_number_of_acts(drama):
            act_count = int(act_temp)
            if scene_temp <= Util.find_number_of_scenes(drama, act_count):
                scene_count = int(scene_temp)
                return True
    return False

def search_for_words_or_phrases():
    global drama, scene_count, act_count
    count = 0
    words = input("Enter words or phrases to search for: ")
    scene_search = extract_scene(scene_count, act_count)
    #search for words or phrases in scene
    for line in scene_search:
        if words.lower() in line.lower():
            count += 1
    print(f"The phrase '{words}' was found {count} time(s) in Act {act_count}, Scene {scene_count}.")


def extract_scene(scene, act):
    global drama
    #get scene lines
    start_idx, end_idx = Util.get_act_scene_bounds(scene, act, drama)
    if start_idx is None or end_idx is None:
        print("Could not locate that scene.")
        return []
    return drama[start_idx:end_idx]


def search_first_and_last_utterance():
    global scene_count, act_count, drama
    character = input("Search for utterances by character: ").strip().upper()
    scene_lines = extract_scene(scene_count, act_count)
    if not scene_lines:
        print("Could not locate that scene.")
        return

    utterances = []
    current_speaker = None
    pattern = re.compile(rf"^{re.escape(character)}\.", re.IGNORECASE)

    for line in scene_lines:
        stripped = line.strip()

        #skip stage directions in square brackets
        if not stripped or stripped.startswith(("ACT ", "Scene ", "[", "Enter", "Exit")):
            continue

        #check for speaker
        if pattern.match(stripped):
            current_speaker = character
            speech = stripped[len(character)+1:].strip()
            if speech:
                utterances.append(speech)
            continue

        #continue with current speaker if we're still in dialogue
        if current_speaker == character:
            if any(stripped.upper().startswith(p + ".") for p in Util.get_character_names(drama)):
                current_speaker = None
                continue
            utterances.append(stripped)

    if utterances:
        print("\nFirst utterance:\n" + utterances[0])
        print("Last utterance:\n" + utterances[-1])
        print("\n")
    else:
        print(f"No utterances found for {character}.")