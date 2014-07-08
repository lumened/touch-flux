#!/usr/bin/python

import time
import json

from src.api_interface import push_notification
import src.gui_interface

#def notify_start():
    
#    line1 = "Touchscreen handler is activated."
#    time_delay = 5000  #in miliseconds
    
#    ('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time_delay, __icon__))


push_notification('Touch for Flux Active', 'Touchscreen handler is now active')

src.gui_interface.start_gui()

while True: src.gui_interface.update_gui()

#pygame.event.Event(QUIT)

#    playback_unit_test()

    
