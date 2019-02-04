class Song:
    """Class to represent a song
    Attribute:
        title(str) - The name of the song
        artist (Artist) - An artist object representing the song creator
        duration (int)- Duration of the song
    """

    def __init__(self, title, artist, duration=0):
        """
        Song Init Method
        Args:
        title:(str) Initializes the title attribute
        artist (str): the artist representing the song creator
        duration: the duration of the song may be zero
        """

        self.title = title
        self.artist = artist
        self.duration = duration

    def get_title(self):
        return self.title

    name = property(get_title)


class Album:
    """Class to represent the Album using it's track lists.

    Attributes:
        name (str): The name of the album
        year (int): The year the album was released
        artist (str): The artist responsible to the album, if not specified,
        the artist will default to an artist with the name "various artist".
        tracks (List[Songs]): A list of songs on the album

        Methods:
            add_Songs : used to add the new songs to the album's track list
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = "various artist"
        else:
            self.artist = artist

        self.tracks = []

    def add_songs(self, song, position=None):
        """
        Add the song to the track list

         song (Song): A song to add
         position (optional[int]): inserting it between other songs if necessary
        otherwise the song will be added to the end  of the list.
        :return:
        """
        song_found = find_object(song, self.tracks)
        if song_found is None:
            song_found = Song(song, self.artist)
            if position is None:
                self.tracks.append(song_found)
            else:
                self.tracks.insert(position, song_found)


class Artist:
    """ Class to store the basic details of an Artist

    Attributes:
        name (str): name of the artist
        album (List[album]): A list of the albums by the artist,
        The list includes only those albums in this collection, it is not
        an exaustive list of the artists published albums.

    Methods:
        add_album: Use to add the album to the artist's current album list
    """

    def __init__(self, name):
        self.name = name
        self.album = []

    def add_album(self, album):
        """Add a new album to the list.

        Args:
            album (Album): Album objet to be added to the list
            if hte album is already added, it will not be added again. (Although this is yet to be implemented)
        """

        self.album.append(album)

    def add_songs(self, name, year, title):
        """Add a new song to the collection of the album

        This method will add the song to the collection of the album
        A new album will be created in the collection if the album does not already exist

        Args:
            name (str): Name of the album
            year (int): year of the album published
            title (str): the title of the song
        """

        album_found = find_object(name, self.album)
        if album_found is None:
            print("Not Found " + name)
            album_found = Album(name, year, self.name)
            self.add_album(album_found)
        else:
            print("Found album "+name)

        album_found.add_songs(title)


def find_object(field, object_list):
    """Check 'object_list' to see if an object with a 'name' attribute equal to 'field' exists, return it if so."""
    for item in object_list:
        if item.name == field:
            return item
    return None


def load_data():
    # new_artist = None
    # new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)

            # if new_artist is None:
            #     new_artist = Artist(artist_field)
            #     artist_list.append(new_artist)
            # elif new_artist.name != artist_field:
            #     # We have just read the details for the new artist
            #     # Store the current album in the current artist collection and then create new artist
            #     new_artist = find_object(artist_field, artist_list)
            #     if new_artist is None:
            #         new_artist = Artist(artist_field)
            #         artist_list.append(new_artist)
            #     # new_artist.add_album(new_album)
            #     # artist_list.append(new_artist)
            #
            #     new_album = None
            #
            # if new_album is None:
            #     new_album = Album(album_field, year_field, new_artist)
            #     new_artist.add_album(new_album)
            # elif new_album.name != album_field:
            #     new_album = find_object(album_field, new_artist.album)
            #     if new_album is None:
            #         new_album = Album(album_field, year_field, new_artist)
            #         new_artist.add_album(new_album)
            #
            # new_song = Song(song_field, new_artist)
            # new_album.add_songs(new_song)
            new_artist = find_object(artist_field, artist_list)
            if new_artist is None:
                new_artist = Artist(artist_field)
                artist_list.append(new_artist)
            new_artist.add_songs(album_field, year_field, song_field)

    return artist_list


def create_checkfile(artist_list):
    with open("checkfile.txt", "w") as checkfile:
        for new_artist in artist_list:
            for new_album in new_artist.album:
                for new_song in new_album.tracks:
                    print("{0.name}\t{1.name}\t{1.year}\t{2.title}".format(new_artist, new_album, new_song), file=checkfile)


if __name__ == '__main__':
    artist = load_data()
    print("There are {} artists present".format(len(artist)))
    create_checkfile(artist)










