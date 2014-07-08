import time
import urllib2
import json

DEBUG = False

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
        if DEBUG : print(volume)
        volume = int(volume) + 5
        method = 'Application.SetVolume'
        parameters = {"volume": volume}
        getJsonRemote(method, parameters)
    except:
        return None


def playback_vol_dec():
    method = 'Application.GetProperties'
    parameters = {"properties": ["volume"]}
    try:
        volume = getJsonRemote(method, parameters)['volume']
        if DEBUG : print(volume)
        volume = int(volume) - 5
        method = 'Application.SetVolume'
        parameters = {"volume": volume}
        getJsonRemote(method, parameters)
    except:
        return None


def playback_find_player():
    method = 'Player.GetActivePlayers'
    player_list = getJsonRemote(method)
    if DEBUG : print(player_list)
    try :
        player_id = player_list[0]['playerid']
        return player_id
    except IndexError or TypeError:
        if DEBUG : print("No players active")
        return None


def playback_toggle_play(): 
    player_id = playback_find_player()
    if player_id == None : return
    method = 'Player.PlayPause'
    parameters = {"playerid": player_id} 
    getJsonRemote(method, parameters)

def playback_rewind(): 
    player_id = playback_find_player()
    if player_id == None : return
    percentage = playback_percentage()
    method = 'Player.Seek'
    parameters = {"playerid": player_id, "value":percentage-3} 
    getJsonRemote(method, parameters)

def playback_forward(): 
    player_id = playback_find_player()
    if player_id == None : return
    percentage = playback_percentage()
    method = 'Player.Seek'
    parameters = {"playerid": player_id, "value":percentage+3} 
    getJsonRemote(method, parameters)

def playback_stop(): 
    player_id = playback_find_player()
    if player_id == None : return
    method = 'Player.Stop'
    parameters = {"playerid": player_id} 
    getJsonRemote(method, parameters)
    
def playback_percentage():
    player_id = playback_find_player()
    if player_id == None : return
    method = 'Player.GetProperties'
    parameters = {"playerid": player_id, "properties":["percentage"]} 
    result = getJsonRemote(method, parameters)
    try:
        return result['percentage']
    except:
        return None

def playback_time():
    player_id = playback_find_player()
    if player_id == None : return
    method = 'Player.GetProperties'
    parameters = {"playerid": player_id, "properties":["time", "totaltime"]} 
    result = getJsonRemote(method, parameters)
    try:
        return json_timetostr(result['time']), json_timetostr(result['totaltime'])
    except:
        return None

def json_timetostr(time):
    s = time['seconds']
    m = time['minutes']
    h = time['hours']
    
    if h==0:
#        if m==0:
#           return '00:' + str("%.2d" % s)
#        else:
        return str("%.2d" % m) + ':' + str("%.2d" % s)
    else:
        return str(h) + ':' + str("%.2d" % m) + ':' + str("%.2d" % s)
    
def playback_title():
    player_id = playback_find_player()
    if player_id == None : return
    method = 'Player.GetItem'
    parameters = {"playerid": player_id, "properties":["title"]} 
    result = getJsonRemote(method, parameters)
    try:
        return result['item']['title']
    except:
        return None



def playback_properties():
    player_id = playback_find_player()
    if player_id == None : return
    method = 'Player.GetProperties'
    parameters = {"playerid": player_id, "properties":["percentage","time"]} 
    result = getJsonRemote(method, parameters)
    return result


def push_notification(title, text):
    method = 'GUI.ShowNotification'
    parameters = {'title':title,'message':text}
    getJsonRemote(method, parameters)
