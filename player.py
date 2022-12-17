from pygame import mixer_music, mixer
from music import Music


class Player:
    """
    Handles how the music will be played
    """
    def __init__(self, library: list[Music]):
        mixer.init()
        self.library = library
        self.current: Music = self.library[0]
        # TODO handle if there is no music in database

    def play_music(self):
        """
        Plays the current music specified in the class.
        At the start it will be the first element in the library
        :return:
        """
        for m in self.library:
            if m.path_to_music == self.current.path_to_music:
                self.current = m
                mixer_music.load(self.current.path_to_music)
                print("Calinan muzik: ", self.current.music_name)
                mixer_music.play()
                break

    def change_music(self, current_music: Music):
        self.current = current_music

    @staticmethod
    def pause_music():
        mixer_music.stop()

    @staticmethod
    def resume_music():
        mixer_music.unpause()

    def previous_music(self):
        previous_index = self.library.index(self.current) - 1
        if previous_index >= 0:
            self.current = self.library[previous_index]
            mixer_music.load(self.current.path_to_music)
