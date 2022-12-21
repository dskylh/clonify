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


def search_music(file_path: str) -> Music:
    file = os.path.splitext(file_path)
    file_name = os.path.basename(file[0])
    results_track = spotify.search(q=file_name, type="track", limit=1)
    tracks = results_track["tracks"]["items"]
    track = tracks[0]
    music_name = track["name"]
    artist = track["artists"][0]["name"]
    album = track["album"]["name"]
    results_artist = spotify.search(q=artist, type="artist")
    genres = results_artist["artists"]["items"][0]["genres"]
    music = Music(music_name, file_path, artist, album, genres[0])
    return music


def search_cover(music: Music) -> str:
    results_album = spotify.search(q=music.album, type="album", limit=1)
    album = results_album["albums"]["items"][0]
    cover_url = album["images"][1]["url"]
    return cover_url


if __name__ == "__main__":
    music = search_music("Silver - Gojira")
    cover = search_cover(music)
