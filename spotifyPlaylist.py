
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json
import os
from dotenv import load_dotenv
from extensions import discussionreplies


load_dotenv()
#scopes
clientID = os.environ["SPOTIPY_CLIENT_ID"]
scope = 'playlist-modify-public'
username = os.environ['user']
redirect = os.environ['SPOTIPY_REDIRECT_URI']

oAuth = SpotifyOAuth(
    scope=scope,
    username=username,
    redirect_uri=redirect,
    client_id=clientID
    )

#auth
spotifyObject = spotipy.Spotify(auth_manager= oAuth)


#create the playlist

#playlistName = 'Mr.Hunns Classroom Beats'
#playlistDesc = 'A class made playlist for programming.'


#spotifyObject.user_playlist_create(
#    user=username,
#    name=playlistName,
#    public=True,
#    description=playlistDesc
#)


# SONGS FROM THE CANVAS DISCUSSION
discussionEntries = discussionreplies.getreplies()

# get the users first playlist and set that as the class playlist
classPlaylist = spotifyObject.user_playlists(user=username)
playlist = classPlaylist['items'][0]['id']



def getAllURIs():
    # returns list of song uris in playlist
    results = spotifyObject.playlist(playlist_id=playlist)
    return [item["track"]["uri"] for item in results["tracks"]["items"]]

uriCache = getAllURIs()

# main function
def main():
    addTo = []
    # iterate through discussion entries
    for i, song in enumerate(discussionEntries):
        result = spotifyObject.search(q=song)
        try:
            # get song uri
            result = result['tracks']['items'][0]['uri']
        except IndexError:
            # if no result of said song iterate to next song
            continue
        
        if result in uriCache:
            # if the song is in the playlist iterate to the next song in the discussion
            continue
        elif result not in uriCache:
            # add song uri to list of songs to add
            addTo.append(result)
    # returns list of songs to add 
    return addTo

songs = main()
# adds songs to the playlist 
spotifyObject.user_playlist_add_tracks(
        user=username,
        playlist_id=playlist,
        tracks=songs
        )








