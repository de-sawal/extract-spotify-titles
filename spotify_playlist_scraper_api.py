import os
import json
import csv
import argparse
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "YOUR_CLIENT_ID"    #replace with youurs
CLIENT_SECRET = "YOUR_CLIENT_SECRET"    #both

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_playlist_tracks(playlist_url_or_id):
    """
    Retrieve all track details from the given Spotify playlist.
    """
    results = sp.playlist_items(playlist_url_or_id)
    tracks = []
    while results:
        for item in results['items']:
            track = item['track']
            if track is None:
                continue
            track_info = {
                'name': track.get('name'),
                'artist': ', '.join([artist['name'] for artist in track.get('artists', [])]),
                'album': track.get('album', {}).get('name'),
                'duration_ms': track.get('duration_ms'),
                'external_url': track.get('external_urls', {}).get('spotify')
            }
            tracks.append(track_info)
        if results.get('next'):
            results = sp.next(results)
        else:
            results = None
    return tracks

def export_to_csv(tracks, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['name', 'artist', 'album', 'duration_ms', 'external_url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for track in tracks:
            writer.writerow(track)

def export_to_json(tracks, filename):
    with open(filename, 'w', encoding='utf-8') as jsonfile:
        json.dump(tracks, jsonfile, indent=4)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Spotify Playlist Scraper using Spotify API")
    parser.add_argument('playlist', help='Spotify Playlist URL or ID')
    parser.add_argument('--export', choices=['csv', 'json'], default='csv', help='Export format (csv or json)')
    parser.add_argument('--output', default='playlist_output', help='Output file name (without extension)')
    args = parser.parse_args()

    tracks = get_playlist_tracks(args.playlist)
    if not tracks:
        print("No tracks found. Check if the playlist is public or if your credentials are correct.")
    else:
        if args.export == 'csv':
            output_file = args.output if args.output.endswith('.csv') else args.output + '.csv'
            export_to_csv(tracks, output_file)
        else:
            output_file = args.output if args.output.endswith('.json') else args.output + '.json'
            export_to_json(tracks, output_file)
        print(f"Exported {len(tracks)} tracks to {output_file}")
