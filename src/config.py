# This is the global data file

# Development Switches

INDEP = True 
DEBUG = False

# Constants

#This is the color scheme
colors = {'orange':(0xFF,0x33,0x00), 'white':(0xFF,0xE6,0xB3), 'maroon':(0x88,0x00,0x00)}

#This identifies the screens
screen_ids = {'navigation':1, 'playback':2, 'camera':3, 'power':4}


# Variables

#During playback, if user switches to navigation then this is used to prevent the system from switching back to the playback screen till the user chooses to do so.
manual_switch = False

#To maintain the state of the projector, may be updated externally
projector = False #Off, by default

#Charging is manually controlled
charging = False

#Maintainst state of power supply
plugged_in = False

#Signals to the application that the screen needs to be redrawn
update_screen = True

