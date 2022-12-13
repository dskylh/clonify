from pygame import mixer_music, mixer
from music import Music
from db import DbConnection


class Player:
    def __init__(self, library: list[Music]):
        mixer.init()
        self.library = library
        self.current: Music = self.library[0]

    def playMusic(self):
        for m in self.library:
            if m.pathToMusic == self.current.pathToMusic:
                self.current = m
                mixer_music.load(self.current.pathToMusic)
                print("Calinan muzik: ", self.current.musicName)
                mixer_music.play()
                break

    def changeMusic(self, currentMusic: Music):
        self.current = currentMusic

    def pauseMusic(self):
        mixer_music.stop()

    def resumeMusic(self):
        mixer_music.unpause()

    def previousMusic(self):
        previousIndex = self.library.index(self.current) - 1
        if previousIndex >= 0:
            self.current = self.library[previousIndex]
            mixer_music.load(self.current.pathToMusic)
