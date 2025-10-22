def get_character_names(drama):
    if drama is None or len(drama) == 0:
        return []

    characters = []
    in_dramatis_section = False

    for line in drama:
        stripped_line = line.strip()

        #checks for dramatis personae section
        if "Dramatis Personæ" in stripped_line:
            in_dramatis_section = True
            continue
        #stops when it reaches the end of the characters section
        if stripped_line.startswith("SCENE:"):
            break

        if in_dramatis_section and len(stripped_line) > 0:
            if not any(c.isupper() for c in stripped_line[:3]):
                continue

            if ',' in stripped_line:
                name = stripped_line.split(',')[0].strip()
                characters.append(name)

    return characters

def find_number_of_acts(drama):
    if drama is None:
        print("No drama loaded.")
        return 0
    acts = 0
    in_contents_section = False

    #gets acts listed in first section of drama
    for line in drama:
        stripped_line = line.strip()

        if stripped_line == "Contents":
            in_contents_section = True
            continue

        if stripped_line == "Dramatis Personæ":
            break
        #counts all acts
        if in_contents_section and stripped_line.startswith("ACT "):
            acts += 1

    return acts


def find_number_of_scenes(drama, act):
    if drama is None:
        print("No drama loaded.")
        return 0

    total_acts = find_number_of_acts(drama)
    if act < 1 or act > total_acts:
        print(f"Invalid act number. Must be between 1 and {total_acts}.")
        return 0

    scenes = 0
    in_target_act = False
    act_numeral = convert_int_to_numerals(act)
    target_act = f"ACT {act_numeral}"

    for line in drama:
        stripped_line = line.strip()

        #enter target act
        if stripped_line == target_act:
            in_target_act = True
            continue

        #stop when it reaches the end of the target act
        if in_target_act and stripped_line.startswith("ACT "):
            break

        #counts all scenes
        if in_target_act and stripped_line.startswith("Scene "):
            scenes += 1

    return scenes


def convert_int_to_numerals(act_number):
    return (
        str(act_number)
        .replace("1", "I")
        .replace("2", "II")
        .replace("3", "III")
        .replace("4", "IV")
        .replace("5", "V")
        .replace("6", "VI")
        .replace("7", "VII")
    )

def validate_drama(temp_drama):
    if temp_drama is None or len(temp_drama) == 0:
        print("Please import a drama first.")
        return False
    else:
        return True

def get_act_bounds(selection, drama):
    numeral = convert_int_to_numerals(selection)
    target = "ACT " + numeral

    dramatis_idx = find_dramatis_index(drama)
    search_start = dramatis_idx + 1 if dramatis_idx is not None else 0

    start = None
    for i in range(search_start, len(drama)):
        line_stripped = drama[i].strip()
        #look for "ACT X" on its own line (not in Contents)
        if line_stripped == target:
            start = i
            break

    if start is None:
        return None, None

    #find the end of the act
    end = len(drama)
    next_act_num = selection + 1
    next_numeral = convert_int_to_numerals(next_act_num)
    next_target = "ACT " + next_numeral

    for j in range(start + 1, len(drama)):
        line_stripped = drama[j].strip()
        if line_stripped == next_target:
            end = j
            break

    return start, end

def get_act_scene_bounds(scene, act, drama):
    start, end = get_act_bounds(act, drama)
    if start is None:
        return None, None
    for i in range(start, end):
        line_stripped = drama[i].strip()
        if line_stripped.startswith("Scene "):
            scene_numeral = line_stripped.split()[1]
            if scene_numeral == scene:
                return i, i + 1
    return None, None

def find_dramatis_index(drama):
    if not drama:
        return None
    for i, line in enumerate(drama):
        if line.strip() == "Dramatis Personæ":
            return i
    return None