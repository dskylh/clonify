from pygame import mixer_music, mixer
from music import Music
from pygame.mixer import Sound


class Player:
    """
    Handles how the music will be played
    """

    def __init__(self, library: list[Music]):
        mixer.init()
        self.library = library
        self.current: Music = self.library[0]
        self.current_duration = Sound(self.current.path_to_music).get_length()
        print(self.current_duration)
        self.is_paused = False
        self.is_playing = False

        # TODO handle if there is no music in database

    def update_current_duration(self):
        self.current_duration = Sound(self.current.path_to_music).get_length()
        print(self.current_duration)

    def play_music(self):
        """
        Plays the current music specified in the class.
        At the start it will be the first element in the library
        :return:
        """
        for m in self.library:
            if m.path_to_music == self.current.path_to_music:
                self.current = m
                if self.is_playing:
                    break
                mixer_music.load(self.current.path_to_music)
                print("Calinan muzik: ", self.current.music_name)
                break
        if not self.is_playing:
            mixer_music.play()
            self.is_playing = True
        else:
            self.toggle_pause()

    def change_music(self, current_music: Music):
        self.current = current_music
        self.current_duration = Sound(self.current.path_to_music).get_length()

    def stop_music(self):
        self.is_playing = False
        mixer_music.fadeout(80)

    def toggle_pause(self):
        if self.is_paused:
            mixer_music.unpause()
            self.is_paused = False
        else:
            mixer_music.pause()
            self.is_paused = True

    def previous_music(self):
        previous_index = self.library.index(self.current) - 1
        if previous_index >= 0:
            self.current = self.library[previous_index]
            self.current_duration = Sound(self.current.path_to_music).get_length()
            mixer_music.load(self.current.path_to_music)
