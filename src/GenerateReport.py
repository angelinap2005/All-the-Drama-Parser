drama = []

def menu(dramaTemp):
    global drama
    check = check_file_loaded(dramaTemp)
    if check:
        drama = dramaTemp
        print("Generating report...")
        generate_report()



def check_file_loaded(dramaTemp):

    if dramaTemp is None or len(dramaTemp) == 0:
        print("Please import a drama first.")
        return False
    else:
        return True

def generate_report():
    print("Number of acts: " + str(find_number_of_acts()))
    print("Number of scenes: " + str(find_number_of_scenes()))
    print("Top 20 words:")
    for counter in range(20):
        print(str(counter + 1) + ". " + list(top_20_words().keys())[counter] + " - " + str(list(top_20_words().values())[counter]) + " time(s)")
    print("Character names: ")
    characters = get_character_names()
    for character in characters:
        print("-- " + character)

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

def top_20_words():
    global drama
    if drama is None:
        print("No drama loaded.")
        return 0
    top_words = {}
    in_contents_section = False
    for line in drama:
        stripped_line = line.strip()
        if stripped_line == "Dramatis Personæ":
            in_contents_section = True
            continue
        if stripped_line == "[_Exit._]":
            break

        if in_contents_section:
            words = stripped_line.split()
            for counter in range(len(words)):
                count = words.count(words[counter])
                top_words[words[counter]] = count
        top_words = dict(sorted(top_words.items(), key=lambda item: item[1], reverse=True))



    return top_words


def get_character_names():
    global drama
    if drama is None or len(drama) == 0:
        return []

    characters = []
    in_dramatis_section = False

    for line in drama:
        stripped_line = line.strip()

        if "Dramatis Personæ" in stripped_line or "Dramatis Personae" in stripped_line:
            in_dramatis_section = True
            continue

        if stripped_line.startswith("SCENE:"):
            break

        if in_dramatis_section and len(stripped_line) > 0:
            if not any(c.isupper() for c in stripped_line[:3]):
                continue

            if ',' in stripped_line:
                name = stripped_line.split(',')[0].strip()
                characters.append(name)

    return characters