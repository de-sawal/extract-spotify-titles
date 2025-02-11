# Spotify Playlist Scraper (API Method)

This Python script uses the official Spotify Web API (via the [spotipy](https://spotipy.readthedocs.io/) library) to scrape any public Spotify playlist for song details. It extracts key information such as track name, artist(s), album, duration, and external URL, then exports the data in either CSV or JSON format.

## Features

- **API-Based:** Uses Spotify’s official API for reliable data retrieval.
- **Detailed Track Info:** Retrieves song name, artist(s), album, duration (in ms), and external Spotify URL.
- **Multiple Export Formats:** Supports exporting data as CSV or JSON.
- **Pagination Handling:** Automatically handles playlists with many tracks.

## Prerequisites

- **Python 3.x**
- **spotipy Library:** Install via pip:
  ```bash
  pip install spotipy
  ```
- **Spotify Developer Credentials:**
  - Create an account or log in at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications).
  - Register an application to obtain your **Client ID** and **Client Secret**.

## Setup

1. **Clone or Download the Repository:**
   ```bash
   git clone https://github.com/de-sawal/extract-spotify-titles.git
   cd extract-spotify-titles
   ```

2. **Install Required Dependencies:**
   ```bash
   pip install spotipy
   ```

3. **Configure Your Spotify Credentials:**
   - Open the script file (`spotify_playlist_scraper_api.py`).
   - Replace the placeholder values for `CLIENT_ID` and `CLIENT_SECRET` with your own credentials.

## Usage

Run the script from the command line with the following arguments:

```bash
python spotify_playlist_scraper_api.py PLAYLIST_URL_OR_ID [--export {csv,json}] [--output OUTPUT_FILE_NAME]
```

- **PLAYLIST_URL_OR_ID:** The URL or ID of the Spotify playlist.
- **--export:** (Optional) Choose the export format (`csv` or `json`). Default is CSV.
- **--output:** (Optional) Specify the output file name (without extension). The script automatically appends the correct extension.

### Example

```bash
python spotify_playlist_scraper_api.py "https://open.spotify.com/playlist/your_playlist_id" --export json --output my_playlist
```

This command will scrape the specified playlist and save the output as `my_playlist.json`.

## Script Details

- **get_playlist_tracks(playlist_url_or_id):**  
  Retrieves all tracks from the playlist by handling pagination with Spotify's API.

- **export_to_csv(tracks, filename):**  
  Exports the list of tracks to a CSV file with the following columns: name, artist, album, duration_ms, external_url.

- **export_to_json(tracks, filename):**  
  Exports the list of tracks to a JSON file.

## Important Notes

- **Playlist Accessibility:**  
  The playlist must be public or accessible with your provided credentials.

- **Rate Limiting:**  
  For very large playlists, be aware of possible API rate limits.

- **Error Handling:**  
  If no tracks are found, ensure that the playlist URL/ID is correct and that the playlist is publicly available.
