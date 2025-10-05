import ImportDrama
import GenerateReport
drama = []
def menu():
    global drama
    while True:  # Keep looping to show menu again
        print("Please select an option:")
        print("1. Import a drama from a text file.")
        print("2. Print a summary report.")
        print("3. Output the summary report to a text file.")
        print("4. View details of a drama act.")
        print("5. Search inside a drama scene.")

        selection = input()

        if selection == "1":
            drama = ImportDrama.menu()
        elif selection == "2":
            GenerateReport.menu(drama)
            pass
        elif selection == "3":
            # Handle option 3
            pass
        elif selection == "4":
            # Handle option 4
            pass
        elif selection == "5":
            # Handle option 5
            pass
        else:
            print("Error: Invalid option.")