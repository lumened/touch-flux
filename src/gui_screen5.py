# This file defines the navigation screen.
# This requires the following procedures:
#  init()
#  draw()
#  handle_event()
import time
import atexit, io, os, picamera, yuv2rgb, picamera, pygame
from gui_button import *
from api_interface import *
import custom_events

DEBUG = True

#some variables defined

def init():
    global menu

    menu = {}
#Defining rectangular buttons
    menu['btn1'] = Button('camera') #go back to navigation window
    menu['btn2'] = Button('left') #navigate left in the videos
    menu['btn3'] = Button('right')#navigate right in the videos
    menu['btn4'] = Button('Settings')#Settings
    menu['surface'] = Button(' ')
    return None

   
def draw(screen, mouse, transparent = 0xFF):
    global menu

    x = 10
    y = 10
 
    height = 80 
    width = 60
    menu['surface'].draw_rect(screen, mouse, (20,20,200,280), (0,0),0)    #surface not becoming transparent
    menu['btn1'].draw_rect(screen, mouse, (x,y,height,width), (x+10,y+20), transparent)
    menu['btn2'].draw_rect(screen, mouse, (x,y+160,height,width), (x+30,y+170+10), transparent)
    menu['btn3'].draw_rect(screen, mouse, (x+220,y+160,height,width), (x+230+20,y+170+10), transparent)
    menu['btn4'].draw_rect(screen, mouse, (x+220,y,height,width), (x+230+5,y+20), transparent)
          #btn.check_hover(mouse)
    return None


def handle_event(mouse):
    global menu

#    if playback_find_player() is not None :
#        pygame.event.post(custom_events.SWITCH_TO_PLAYBACK)

    if menu['btn1'].obj.collidepoint(mouse):
        if DEBUG : print('button 1 clicked')
        pygame.event.post(custom_events.SWITCH_TO_NAVIGATION)
#        return 2
            
    elif menu['btn2'].obj.collidepoint(mouse):
        if DEBUG : print('button 2 clicked')
                  
    elif menu['btn3'].obj.collidepoint(mouse):
        if DEBUG : print('button 3 clicked')
        record()          

    elif menu['btn4'].obj.collidepoint(mouse):
        if DEBUG : print('button 4 clicked')
             
    elif menu['surface'].obj.collidepoint(mouse):
        if DEBUG : print('surface clicked')
        record()
    return None
