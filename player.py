from pygame import mixer
from music import Music


class Player:
    def __init__(self, library: list[Music]):
        self.library = library
        self.current:Music

    def playMusic(self, music: Music):
        for m in self.library:
            if m.musicName == music.musicName:
                self.current = m
                mixer.music.load(self.current.pathToMusic)
                mixer.music.play()


    def pauseMusic(self):
        mixer.music.stop()

    def resumeMusic(self):
        mixer.music.unpause()

    def previousMusic(self):
        previousIndex = self.library.index(self.current) - 1
        self.current = self.library[previousIndex]
        mixer.music.load(self.current.pathToMusic)








