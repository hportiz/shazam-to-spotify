from shazam_parser import parse_shazam_log
from spotify_auth import get_spotify_client
from spotify_search import search_track
from spotify_playlist import create_playlist, add_tracks

def main():
    sp = get_spotify_client()

    songs = parse_shazam_log()

    track_ids = []
    for song in songs:
        track_id = search_track(sp, song["query"])
        if track_id:
            track_ids.append(track_id)

    playlist_id = create_playlist(sp, "Shazam Playlist", public=False)
    add_tracks(sp, playlist_id, track_ids)

    print(f"Added {len(track_ids)} tracks to playlist")

if __name__ == "__main__":
    main()