drama = []

def menu(temp_drama):
    success = validate_drama(temp_drama)
    if success:
        get_act_from_drama()

def validate_drama(temp_drama):
    if temp_drama is None or len(temp_drama) == 0:
        print("Please import a drama first.")
        return False
    else:
        global drama
        drama = temp_drama
        return True


def get_act_from_drama():
    print("Please enter the act number:")
    selection = input()
    if selection.isdigit():
        selection = int(selection)
        if selection <= find_number_of_acts():
            print("Act " + str(selection) + " details:")
            for line in drama:
                if line.startswith("ACT " + convert_int_to_numerals(selection)):
                    start, end = get_act_bounds(selection)
                    for i in range(start, end):
                        print(drama[i])
                    break
        else:
            print("Invalid act number.")


def find_number_of_acts():
    global drama
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

# python
def find_dramatis_index():
    global drama
    if not drama:
        return None
    for i, line in enumerate(drama):
        if line.strip() == "Dramatis Personæ":
            return i
    return None

def get_act_bounds(selection):
    numeral = convert_int_to_numerals(selection)
    target = "ACT " + numeral

    dramatis_idx = find_dramatis_index()
    search_start = dramatis_idx + 1 if dramatis_idx is not None else 0

    start = None
    for i in range(search_start, len(drama)):
        if drama[i].strip().startswith(target):
            start = i
            break

    if start is None:
        return None, None

    end = len(drama)
    for j in range(start + 1, len(drama)):
        if drama[j].strip().startswith("ACT "):
            end = j
            break

    return start, end

def extract_between_acts(start_act, end_act=None):
    global drama
    start_idx, _ = get_act_bounds(start_act)
    if start_idx is None:
        return []

    if end_act is None:
        end_idx = len(drama)
    else:
        end_idx, _ = get_act_bounds(end_act)
        if end_idx is None:
            end_idx = len(drama)

    return drama[start_idx:end_idx]
