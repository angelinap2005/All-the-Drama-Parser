import Util

drama = []
drama_reports = {}

def menu(drama_temp):
    global drama
    check = check_file_loaded(drama_temp)
    if check:
        drama = drama_temp
        print("Generating report...")
        generate_report()


def check_file_loaded(drama_temp):
    #check if the user has loaded a file
    if drama_temp is None or len(drama_temp) == 0:
        print("Please import a drama first.")
        return False
    else:
        return True


def generate_report():
    global drama
    try:
        #in a try catch block to prevent errors from crashing the program
        #get title for readability
        title = get_drama_title()
        print("Title: " + title)
        num_acts = Util.find_number_of_acts(drama)
        num_scenes = find_number_of_scenes()
        print("Number of acts: " + str(num_acts))
        print("Number of scenes: " + str(num_scenes))
        print("Top 20 words:")
        top_20 = top_20_words()
        for i, (word, freq) in enumerate(top_20.items()):
            if i >= 20:
                break
            print(f"{i + 1}. {word} - {freq} time(s)")
        print("Character names: ")
        characters = Util.get_character_names(drama)
        for character in characters:
            print("-- " + character)
        save_report(num_acts, num_scenes, top_20, characters)
    except IndexError:
        print("Error while generating report.")
        return


def find_number_of_scenes():
    global drama
    if drama is None:
        print("No drama loaded.")
        return 0
    scenes = 0
    in_contents_section = False
    #checks for number of scenes in drama
    for line in drama:
        stripped_line = line.strip()
        if stripped_line == "Contents":
            in_contents_section = True
            continue
        if stripped_line == "Dramatis Personæ":
            break
        #counts all scenes
        if in_contents_section and stripped_line.startswith("Scene "):
            scenes += 1
    return scenes


def top_20_words():
    global drama
    if not drama:
        print("No drama loaded.")
        return {}

    word_counts = {}
    in_dialogue = False

    for line in drama:
        stripped = line.strip()

        #start counting after Dramatis Personæ
        if stripped == "Dramatis Personæ":
            in_dialogue = True
            continue

        #stop when reaching Project Gutenberg footer
        if "*** END OF THE PROJECT GUTENBERG EBOOK" in stripped:
            break

        #skip non-dialogue content
        if not in_dialogue or stripped.startswith(("ACT ", "Scene ", "[", "Enter", "Exit")):
            continue

        #count words
        for word in stripped.split():
            clean = word.strip(".,;:!?\"'()[]").lower()
            if clean:
                word_counts[clean] = word_counts.get(clean, 0) + 1

    #sort descending
    top_20 = dict(sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:20])
    return top_20



def get_drama_title():
    global drama
    if drama is None or len(drama) == 0:
        print("No drama loaded.")
        return "Unknown Drama"

    #looks for "The Project Gutenberg eBook of" line
    for line in drama:
        if "The Project Gutenberg eBook of" in line:
            # Extract everything after "of "
            parts = line.split("of ", 1)
            if len(parts) > 1:
                return parts[1].strip()

    for i, line in enumerate(drama):
        if line.startswith("Title:"):
            return line.split("Title:", 1)[1].strip()

    #fallback if no title found
    return "Unknown Drama"


def save_report(num_acts, num_scenes, top_20_words_list, characters):
    title = get_drama_title()
    #adds report to dictionary
    drama_report = {"title": title, "num_acts": num_acts, "num_scenes": num_scenes,
                    "top_20_words": top_20_words_list, "characters": characters}
    global drama_reports
    #sets global variable to store reports
    drama_reports[title] = drama_report
    print(f"Report saved with title: '{title}'")
    return


def get_drama_report(title):
    global drama_reports
    return drama_reports.get(title, None)


def get_available_reports():
    #returns a list of all available reports
    global drama_reports
    return list(drama_reports.keys())