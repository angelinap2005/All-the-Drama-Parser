import os

def menu():
    file = select_drama()
    return import_drama(file)


def select_drama():
    valid = False
    #check if the user has entered a file name

    while not valid:
        print("Please enter a drama, or enter 'exit' to exit:")
        selection = input()
        if len(selection) > 0:
            if not os.path.isfile(selection) or not selection.lower().endswith(".txt"):
                if selection.lower() == "exit":
                    print("Exiting file input...")
                    return None
                else:
                    print("Error: Invalid file name. Please try again.")
            else:
                valid = True
                return selection
    return None


def import_drama(drama_file):
    if drama_file is None:
        return None
    path = drama_file if os.path.isabs(drama_file) else os.path.join(os.getcwd(), drama_file)
    drama = []
    print("Importing drama...")
    try:
        with open(path, "r", encoding="utf-8") as file:
            for line in file:
                drama.append(line.strip())
    except FileNotFoundError:
        print("Error: File not found.")
        return None
    except UnicodeDecodeError:
        print("Error: File is not encoded in UTF-8.")
        return None

    # Check for 'act' and 'scene' anywhere in any line (case-insensitive)
    has_act = any("act" in (line or "").lower() for line in drama)
    has_scene = any("scene" in (line or "").lower() for line in drama)

    if has_act and has_scene:
        print("Drama imported successfully.")
        return drama
    else:
        print("Error: Invalid drama file.")
        return None
