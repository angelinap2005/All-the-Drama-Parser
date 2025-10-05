drama = []

def menu(dramaTemp):
    global drama
    check = check_file_loaded(dramaTemp)
    if check:
        drama = dramaTemp
        print("Generating report...")
        generate_report()



def check_file_loaded(dramaTemp):

    if dramaTemp is None:
        print("Please import a drama first.")
        return False
    else:
        return True

def generate_report():
    print("Number of acts: " + str(find_number_of_acts()))
    print("Number of scenes: " + str(find_number_of_scenes()))

def find_number_of_acts():
    global drama
    if drama is None:
        print("No drama loaded.")
        return 0
    acts = 0
    in_contents_section = False

    for line in drama:
        stripped_line = line.strip()

        if stripped_line == "Contents":
            in_contents_section = True
            continue

        if stripped_line == "Dramatis Personæ":
            break

        if in_contents_section and stripped_line.startswith("ACT "):
            acts += 1

    return acts

def find_number_of_scenes():
    global drama
    if drama is None:
        print("No drama loaded.")
        return 0
    scenes = 0
    in_contents_section = False
    for line in drama:
        stripped_line = line.strip()
        if stripped_line == "Contents":
            in_contents_section = True
            continue
        if stripped_line == "Dramatis Personæ":
            break
        if in_contents_section and stripped_line.startswith("Scene "):
            scenes += 1
    return scenes

