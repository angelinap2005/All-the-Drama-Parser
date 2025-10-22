import Util

drama = []
scene = 0
act = 0

def menu(drama_temp):
    global drama
    success = Util.validate_drama(drama_temp)
    if success:
        drama = drama_temp
    if prompt_for_scene_and_act():
        search_for_words_or_phrases()

    prompt_for_scene_and_act()

def prompt_for_scene_and_act():
    global scene, act
    scene_temp = input("Enter scene number: ")
    act_temp = input("Enter act number: ")
    if scene_temp.isdigit() and act_temp.isdigit():
        scene_temp = int(scene_temp)
        act_temp = int(act_temp)
        if act_temp <= Util.find_number_of_acts(drama):
            act = int(act_temp)
            if scene_temp <= Util.find_number_of_scenes(drama, act):
                scene = int(scene_temp)
                return True
    return False

def search_for_words_or_phrases():
    global drama, scene, act
    count = 0
    words = input("Enter words or phrases to search for: ")
    scene_search = extract_scene(scene, act)
    for line in scene_search:
        if words in line:
            count += 1
    print(f"The phrase '{words}' was found {count} time(s) in Act {act}, Scene {scene}.")


def extract_scene(scene, act):
    global drama
    start_idx, end_idx = Util.get_act_scene_bounds(scene, act, drama)
    return drama[start_idx:end_idx]