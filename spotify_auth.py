import spotipy
from spotipy.oauth2 import SpotifyOAuth


def get_spotify_client():
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            client_id="client-id-goes-here",
            client_secret="-client-secret-goes-here",
            redirect_uri="http://127.0.0.1:8888/callback",
            scope="playlist-modify-private playlist-modify-public",
            open_browser=True
        )
    )
    return sp

