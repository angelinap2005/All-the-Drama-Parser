import Util

drama = []

def menu(drama_temp):
    global drama
    success = Util.validate_drama(drama_temp)
    if success:
        drama = drama_temp