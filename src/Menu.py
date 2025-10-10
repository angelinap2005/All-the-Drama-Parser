import ImportDrama
import GenerateReport
import SaveReportToFile

drama = []

def menu():
    global drama
    while True:
        #keeps looping until user selects a valid option
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
        elif selection == "3":
            #list all available reports
            available_reports = GenerateReport.get_available_reports()
            if len(available_reports) == 0:
                print("No reports available. Please generate a report first (option 2).")
                continue

            print("Available reports:")
            #prints available reports for user to choose from
            for idx, title in enumerate(available_reports, 1):
                print(f"{idx}. {title}")

            print("Enter the number of the report you want to save (or type the exact title):")
            user_input = input().strip()

            #ensure the user input is a valid number or title
            if user_input.isdigit():
                report_idx = int(user_input) - 1
                if 0 <= report_idx < len(available_reports):
                    title = available_reports[report_idx]
                else:
                    print("Error: Invalid report number.")
                    continue
            else:
                title = user_input

            #try to find the report by title
            report = GenerateReport.get_drama_report(title)
            if report is None:
                print(f"Error: No report found with title '{title}'.")
            else:
                SaveReportToFile.menu(report)
        elif selection == "4":
            # Handle option 4
            pass
        elif selection == "5":
            # Handle option 5
            pass
        else:
            print("Error: Invalid option.")