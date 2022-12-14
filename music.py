class Music:
    """
    Holds the information about the musics.
    """

    def __init__(self, music_name, path_to_music, artist="", album="", genre=""):
        self.music_name = music_name
        self.artist = artist
        self.album = album
        self.genre = genre
        self.path_to_music = path_to_music

    def __str__(self):
        return f"""
Music Name = {self.music_name}
Artist = {self.artist}
Album = {self.album}
Genre = {self.genre}
Path to Music = {self.path_to_music}
        """
