# This is the global data file

# Development Switches

INDEP = True 
DEBUG = True

# Constants

#This is the color scheme
colors = {'orange':(0xFF,0x33,0x00), 'transparent':(0xFF,0xE6,0xB3), 'white':(0xFF,0xE6,0xB3), 'maroon':(0x88,0x00,0x00)}

#This identifies the screens
screen_ids = {'navigation':1, 'playback':2, 'camera':3, 'power':4, 'camera_settings':5}


# Variables

#During playback, if user switches to navigation then this is used to prevent the system from switching back to the playback screen till the user chooses to do so.
manual_switch = False

#to determine whether video is being recorded or not
recording = False

#to determine whether preview is on or not
camera_preview = False

#determine the resolution of the camera
mode = 1
#sizeMode = 1

# max_count = to keep a measure of the total no of files
max_count = 0
# count = determines the number of the file on which we are current$
count = 0

#path of the recorded videos
path = "/home/pi/recorded_videos"

#a variable to determine the start time of recording
start_time = None

#To maintain the state of the projector, may be updated externally
projector = True #Off, by default

#Charging is automated
charging = False

#Maintainst state of power supply
plugged_in = False

#Signals to the application that the screen needs to be redrawn
update_screen = True
