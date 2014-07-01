import time
import urllib2
import json

from api_wrapper import *

'''
    Navigation Functions
    - Up, Down, Left and Right for basic navigation
    - Select to enter an element
    - Back to return to previous level
'''

def nav_up():
    method = 'Input.Up'
    getJsonRemote(method)

def nav_down():
    method = 'Input.Down'
    getJsonRemote(method)

def nav_left():
    method = 'Input.Left'
    getJsonRemote(method)

def nav_right():
    method = 'Input.Right'
    getJsonRemote(method)

def nav_select():
    method = 'Input.Select'
    getJsonRemote(method)

def nav_back():
    method = 'Input.Back'
    getJsonRemote(method)

'''
    Playback Functions
    - Play/Pause
    - Volume Control
'''

def playback_vol_inc():
    method = 'Application.GetProperties'
    parameters = {"properties": ["volume"]}
    try:
        volume = getJsonRemote(method, parameters)['volume']
        print(volume)
        volume = int(volume) + 5
        method = 'Application.SetVolume'
        parameters = {"volume": volume}
        getJsonRemote(method, parameters)
    except:
        return


def playback_vol_dec():
    method = 'Application.GetProperties'
    parameters = {"properties": ["volume"]}
    try:
        volume = getJsonRemote(method, parameters)['volume']
        print(volume)
        volume = int(volume) - 5
        method = 'Application.SetVolume'
        parameters = {"volume": volume}
        getJsonRemote(method, parameters)
    except:
        return


def playback_find_player():
    method = 'Player.GetActivePlayers'
    player_list = getJsonRemote(method)
    print(player_list)
    try :
        player_id = player_list[0]['playerid']
        return player_id
    except IndexError:
        print("No players active")
        return


def playback_toggle_play(): 
    player_id = playback_find_player()
    if player_id == None : return
    method = 'Player.PlayPause'
    parameters = {"playerid": player_id} 
    getJsonRemote(method, parameters)
    

#Not functional atm
def playback_status():
    player_id = playback_find_player()
    if player_id == None : return
    request = '{"jsonrpc": "2.0", "method": "Player.GetItem", "params": { "properties": ["title", "album", "artist", "duration", "thumbnail", "file", "fanart", "streamdetails"], "playerid":' + str(player_id) +  ' }, "id": "AudioGetItem"}'
    current = xbmc.executeJSONRPC(request)
    title = json.JSONDecoder().decode(current)['result']['item']['title']
    #print title
    return title
