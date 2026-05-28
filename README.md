# Shazam to Spotify

Generates Spotify playlists by parsing Shazam JSON files.

---

## Motivation

 I aimed to automate the process of identifying a song,  opening Spotify, searching, verifying it's the right track, saving it, and adding it to a playlist. Manually doing this for one song is pain free, but doing that for dozens of entries is tedious and doesn't scale well. This project automates that entire process. Export your Shazam history, run the program, and a Spotify playlist is created for you automatically.

---

### Getting the Shazam Data

The first challenge was exporting Shazam records into a usable format. After considering options like hosting a file server for uploads, the simpler approach was to build a custom iOS Shortcut that runs whenever Shazam identifies a song. The shortcut appends the song's title, artist, URLs, and timestamp to a formatted text file (`shazam_log.txt`). That file gets AirDropped to the computer and fed into the application.

### The Application

The project is split into four modules:

- **`shazam_parser.py`** — Reads `shazam_log.txt` and parses each entry into key-value pairs. Handles normalization like stripping featured artist tags to improve search accuracy.
- **`spotify_auth.py`** — Handles Spotify API authentication via SpotifyOAuth using the Spotipy library.
- **`spotify_search.py`** — Searches Spotify for each parsed song and returns the track ID if found.
- **`spotify_playlist.py`** — Creates a new Spotify playlist and adds all matched tracks to it.

`main.py` ties everything together — it authenticates, parses the log, searches for each track, and builds the playlist in one run.

---

## Setup

### Requirements

- Python 3.x
- [Spotipy](https://spotipy.readthedocs.io/) — `pip install spotipy`

### Spotify Developer Credentials

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) and create an application.
2. Copy your **Client ID** and **Client Secret**.
3. Paste your credentials into `spotify_auth.py`:


### Running the Application

1. AirDrop or copy your `shazam_log.txt` into the project folder.
2. Run main.py
3. A browser window will open for Spotify authentication. Log in and authorize the app.
4. The playlist will be created in your Spotify account.

---

## What I Learned

This project was a great introduction to working with third-party APIs and OAuth authentication. Getting SpotifyOAuth to work correctly was the biggest challenge and required troubleshooting the redirect URI configuration and token handling. It also reinforced how powerful Python libraries like Spotipy can be.

---

## Future Ideas

- Automate the log file transfer so AirDrop is no longer a manual step
- Filter songs by timestamp so only recent Shazam entries are added
- Add a GUI for a better user experience
