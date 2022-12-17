from dotenv import load_dotenv
import os
from music import Music
import spotipy
from spotipy import SpotifyClientCredentials

load_dotenv()

client_id = os.environ["SPOTIPY_CLIENT_ID"]
client_secret = os.environ["SPOTIPY_CLIENT_SECRET"]
redirect_uri = os.environ["SPOTIPY_REDIRECT_URI"]
spotify = spotipy.Spotify(auth_manager=SpotifyClientCredentials())


def search_music(music: Music):
    # todo implement
    return "todo"