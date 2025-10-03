def menu():
    file = select_drama()
    import_drama(file)


def select_drama():
    print("Please enter a drama:")
    selection = input()

    if len(selection) > 0:
        if not selection.endswith(".txt"):
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
        path = "C:/Users/angel/OneDrive - University of Strathclyde/Year 3/CS353/programmingProjects/PythonProject/coursework1/files/" + drama_file

        if drama_file is not None:
            print("Importing drama...")
            with open(path, "r", encoding="utf-8") as file:
                for line in file:
                    drama.append(line.strip())
            return drama
        return None
