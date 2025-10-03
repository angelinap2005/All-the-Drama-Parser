import ImportDrama

def menu():
    print("Please select an option:")
    print("1. Import a drama from a text file.")
    print("2. Print a summary report.")
    print("3. Output the summary report to a text file.")
    print("4. View details of a drama act.")
    print("5. Search inside a drama scene.")

    selection = input()

    if selection == "1":
        ImportDrama.menu()
    elif selection == "2":
        return 2
    elif selection == "3":
        return 3
    elif selection == "4":
        return 4
    elif selection == "5":
        return 5
    else:
        return -1
    return

menu()