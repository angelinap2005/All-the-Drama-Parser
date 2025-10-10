report = {}


def menu(temp_report):
    global report
    report = temp_report
    create_report_file()


def create_report_file():
    global report
    filename = input("Please enter a filename to save the report to: ")
    with open(filename, "w") as file:
        file.write("Title: " + report["title"] + "\n")
        file.write("Number of acts: " + str(report["num_acts"]) + "\n")
        file.write("Number of scenes: " + str(report["num_scenes"]) + "\n")
        file.write("Top 20 words:\n")

        #gets top 20 words from report
        top_words = report["top_20_words"]
        if isinstance(top_words, dict):
            #converts dictionary to list of tuples
            word_items = list(top_words.items())

        for word in word_items[:20]:
            #ensures that the word is a tuple or list with at least two elements
            if isinstance(word, (tuple, list)) and len(word) >= 2:
                file.write(str(word[0]) + ": " + str(word[1]) + "\n")
            else:
                #fallback: format is unknown
                continue

        file.write("Characters:\n")

        #add characters to report
        if "characters" in report:
            for character in report["characters"]:
                file.write("-- " + str(character) + "\n")

    #inform user that report was saved successfully
    print(f"Report saved successfully to {filename}")