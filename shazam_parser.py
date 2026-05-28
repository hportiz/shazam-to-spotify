import os
import re
from pprint import pprint


def parse_shazam_log():

    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "shazam_log.txt")

    songs = []
    normalized = []
    
    with open(file_path) as f:
        entries = f.read().strip().split("___")
    
        for entry in entries:
            if not entry.strip():
                continue

            entry_dict = {}
            lines = entry.splitlines()

            for line in lines:
                if not line.strip():
                    continue

                key, value = line.split(":", 1)
                entry_dict[key.strip()] = value.strip()

            normalized.append(normalize_song(entry_dict))
            
        return normalized

def normalize_song(song):
    title = song.get("Title", "")
    artist = song.get("Artist", "")

    #remove feature
    title = re.sub(r"\(feat\..*?\)", "", title, flags=re.IGNORECASE)

    title = title.lower().strip()
    artist = artist.lower().strip()

    return {
        "title": title,
        "artist": artist,
        "query": f"{title} {artist}"
    }
