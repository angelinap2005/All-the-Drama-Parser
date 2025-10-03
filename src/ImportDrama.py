def select_drama():
    print("Please select a drama:")
    print("1. A Midsummer Night's Dream")
    print("2. Othello the Moor of Venice")
    print("3. Romeo and Juliet")

    selection = input()
    if selection == "1":
        return "files/A Midsummer Night's Dream.txt"
    elif selection == "2":
        return "files/Othello the Moor of Venice.txt"
    elif selection == "3":
        return "files/Romeo and Juliet.txt"
    else:
        return None

def import_drama(drama_file):
    drama = []
    if drama_file is not None:
        with open(drama_file, "r") as file:
            for line in file:
                drama.append(line.strip())
        return drama
    return None