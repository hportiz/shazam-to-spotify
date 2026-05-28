def create_playlist(sp, name, public=False):
    user = sp.current_user()
    playlist = sp.user_playlist_create(user=user["id"], name=name, public=public)
    return playlist["id"]

def add_tracks(sp, playlist_id, track_ids):
    if not track_ids:
        print("No tracks to add.")
        return

    sp.playlist_add_items(playlist_id, track_ids)
