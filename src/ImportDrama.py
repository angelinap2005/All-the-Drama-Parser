def select_drama():
    print("Please enter a drama:")
    selection = input()

    length = len(selection)
    if length > 0:
        if selection[:-length] is not ".txt":
            return None
        else:
            return selection
    else:
        return None

def import_drama(drama_file):
    drama = []

    if drama_file is None:
        return None
    else:
        path = "files/" + drama_file

    if path is None:
        return None

    if drama_file is not None:
        with open(drama_file, "r") as file:
            for line in file:
                drama.append(line.strip())
        return drama
    return None