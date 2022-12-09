from pygame import mixer
from music import Music




def playMusic(music: Music):
    mixer.load(music.pathToMusic)
    mixer.play()

if __name__ == '__main__':
    playMusic()
