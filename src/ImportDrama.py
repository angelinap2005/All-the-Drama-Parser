def menu():
    file = select_drama()
    return import_drama(file)


def select_drama():
    print("Please enter a drama:")
    selection = input()

    #check if the user has entered a file name
    if len(selection) > 0:
        if not selection.endswith(".txt"):
            return None
        else:
            return selection
    else:
        return None


def import_drama(drama_file):
    if drama_file is None:
        return None
    #default path to the files
    path = "C:/Users/angel/OneDrive - University of Strathclyde/Year 3/CS353/programmingProjects/PythonProject/coursework1/files/" + drama_file
    drama = []
    #imports file if a valid path is given
    print("Importing drama...")
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            drama.append(line.strip())

    return drama