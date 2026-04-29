def create_song_files(path, text):
    my_list = text.split(' ')
    my_list.sort()

    with open(path, 'w', encoding="utf-8") as file:
        for song in my_list:
            file.write(song + "\n")
            print(song)
        
songs = "Hola Aurora Adios Morire"
create_song_files('songs.txt', songs)