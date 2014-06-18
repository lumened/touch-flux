import time
import json

from api_interface import *
from gui_interface import *

def notify_start():
    
    line1 = "Touchscreen handler is activated."
    time_delay = 5000  #in miliseconds
    
#    ('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time_delay, __icon__))


#Add-on Execution Starts
#notify_start()   
start_gui()

while (True): update_gui()

#pygame.event.Event(QUIT)

#    playback_unit_test()

    
