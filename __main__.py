#!/usr/bin/python

import time
import json

from src.api_interface import push_notification
import src.gui_interface
import src.api_projector
import src.config

#def notify_start():
    
#    line1 = "Touchscreen handler is activated."
#    time_delay = 5000  #in miliseconds
    
#    ('Notification(%s, %s, %d, %s)'%(__addonname__,line1, time_delay, __icon__))


if src.config.projector: push_notification('Touch for Flux Active', 'Touchscreen handler is now active')

src.api_projector.init_projector()
src.gui_interface.start_gui()

while True: src.gui_interface.update_gui()

#pygame.event.Event(QUIT)

#    playback_unit_test()

    
