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


def search_music(file_path: str):
    file_name = os.path.splitext(file_path)
    results_track = spotify.search(q=file_name, type="track", limit=1)
    results_artist = spotify.search(q=file_name, type="artist")

    tracks = results_track["tracks"]["items"]
    artists = results_artist["artists"]["items"]
    track = tracks[0]
    for artist in artists:
        print(artist["genres"])
    music_name = track["name"]
    artist = track["artists"][0]["name"]
    album = track["album"]["name"]
    # genre = track["artists"][0]["genres"][0]


search_music("Gojira")
