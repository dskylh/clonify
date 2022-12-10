from pygame import mixer_music, mixer
from music import Music
from db import DbConnection


class Player:
    def __init__(self, library: list[Music]):
        self.current = None
        self.library = library
        self.current: Music

    def playMusic(self, music: Music):
        for m in self.library:
            if m.musicName == music.musicName:
                self.current = m
                mixer_music.load(self.current.pathToMusic)
                mixer_music.play()
                print("bruh")

    def pauseMusic(self):
        mixer_music.stop()

    def resumeMusic(self):
        mixer_music.unpause()

    def previousMusic(self):
        previousIndex = self.library.index(self.current) - 1
        self.current = self.library[previousIndex]
        mixer_music.load(self.current.pathToMusic)


if __name__ == '__main__':


