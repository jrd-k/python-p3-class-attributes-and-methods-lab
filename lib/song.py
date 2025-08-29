# lib/song.py

class Song:
    # ----- Class attributes -----
    count = 0
    artists = []
    genres = []
    genre_count = {}
    artist_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # When a new song is created:
        self.add_song_to_count()
        self.add_to_artists(artist)
        self.add_to_genres(genre)
        self.add_to_genre_count(genre)
        self.add_to_artist_count(artist)

    # ----- Class methods -----
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_artists(cls, artist):
        # Add only if unique
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genres(cls, genre):
        # Add only if unique
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_genre_count(cls, genre):
        # Increment genre count histogram
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artist_count(cls, artist):
        # Increment artist count histogram
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1
