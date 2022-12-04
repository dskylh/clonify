class Music:
    def __init__(self, musicName: str, pathToMusic: str, artist="", album="", genre=""):
        self.musicName = musicName
        self.artist = artist
        self.album = album
        self.genre = genre
        self.pathToMusic = pathToMusic
