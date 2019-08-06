import os
import sys
import json
import spotipy
import webbrowser
import spotipy.util as util
from json.decoder import JSONDecodeError

def addSongToPlaylist(spotifyURI, playlist):
    os.environ['SPOTIPY_CLIENT_ID'] = clientID
    os.environ['SPOTIPY_CLIENT_SECRET'] = clientsecret
    os.environ['SPOTIPY_REDIRECT_URI'] = 'http://www.google.com/'
    songArr = spotifyURI
    for i in range(len(spotifyURI)):
        songArr[i] = spotifyURI[i].split(':')[2]
    #playArr = ['4Eh0EtBQSbUtTyQ7KTwbib','4Eh0EtBQSbUtTyQ7KTwbib','4Eh0EtBQSbUtTyQ7KTwbib']
    #songArr = ['7ndgQ4LPJwaF4o6QHLaq9i', '4TxJQDtvYHJcOBH6ONi6q2', '68ya2rV2ssI5cssu1B5XBx']

    username = user
    scope = playlist
    client_id = clientID
    client_secret = clientsecret
    redirect_uri = 'http://www.google.com/'
    util.prompt_for_user_token(username,scope,client_id,client_secret,redirect_uri)



    token = util.prompt_for_user_token(username, scope)
    for i in range(len(songArr)):
        if token:
            sp = spotipy.Spotify(auth=token)
            sp.trace = False
            results = sp.user_playlist_add_tracks(username, playlist[i], [songArr[i]])
            print( results)
        else:
            print( "Can't get token for", username)

