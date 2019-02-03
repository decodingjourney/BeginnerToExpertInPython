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
        :param title:(str) Initializes the title attribute
        :param artist: the artist object representing the song creator
        :param duration: the duration of the song may be zero
        """

        self.title = title
        self.artist = artist
        self.duration = duration


class Album:
    """Class to represent the Album using it's track lists.

    Attributes:
        name (str): The name of the album
        year (int): The year the album was released
        artist (Artist): The artist responsible to the album, if not specified,
        the artist will default to an artist with the name "various artist".
        tracks (List[Songs]): A list of songs on the album

        Methods:
            add_Songs : used to add the new songs to the album's track list
    """

    def __init__(self, name, year, artist=None):
        self.name = name
        self.year = year
        if artist is None:
            self.artist = Artist("various artist")
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

        if position is None:
            self.tracks.append(song)
        else:
            self.tracks.insert(position, song)


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





def load_data():
    new_artist = None
    new_album = None
    artist_list = []

    with open("albums.txt", "r") as albums:
        for line in albums:
            artist_field, album_field, year_field, song_field = tuple(line.strip('\n').split('\t'))
            year_field = int(year_field)
            print(artist_field, album_field, year_field, song_field)

            if new_artist is None:
                new_artist = Artist(artist_field)
            elif new_artist.name != artist_field:
                # We have just read the details for the new artist
                # Store the current album in the current artist collection and then create new artist
                new_artist.add_album(new_album)
                artist_list.append(new_artist)
                new_artist = Artist(artist_field)
                new_album = None

            if new_album is None:
                new_album = Album(album_field, year_field, new_artist)
            elif new_album.name != album_field:
                new_artist.add_album(new_album)
                new_album = Album(album_field, year_field, new_artist)


if __name__ == '__main__':
    load_data()









