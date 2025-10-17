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