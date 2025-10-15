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
        if selection <= find_number_of_acts():
            print("Act " + selection + " details:")
            for line in drama:
                if line.startswith("ACT " + selection):
                    print(line)
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
