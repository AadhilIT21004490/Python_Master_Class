
song = "shape OF You"

artist = "tommas shElbY"

def format_music():
    music_1 = song.replace(" ","_").capitalize() + " By " + artist.capitalize()
    return music_1

print(format_music())
