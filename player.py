from pygame import mixer_music as mixer
from music import Music




def playMusic(music: Music):
    mixer.load(music.pathToMusic)
    mixer.play()

if __name__ == '__main__':
    playMusic()