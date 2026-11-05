def make_album(artist, title, songs=None):
    album = {
        'artist': artist,
        'title': title
    }

    if songs:
        album['songs'] = songs

    return album


while True:
    print("\nEnter album information (or 'q' to quit).")

    artist = input("Artist: ")

    if artist == 'q':
        break

    title = input("Album title: ")

    if title == 'q':
        break

    print(make_album(artist, title))