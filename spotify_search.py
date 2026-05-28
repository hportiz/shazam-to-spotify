def search_track(sp, query):
    results = sp.search(q=query, type="track", limit=1)

    tracks = results.get("tracks", {}).get("items", [])
    if not tracks:
        return None

    return tracks[0]["id"]