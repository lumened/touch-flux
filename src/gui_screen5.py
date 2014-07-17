# This file defines the navigation screen.
# This requires the following procedures:
#  init()
#  draw()
#  handle_event()
import time, datetime
import atexit, io, os, picamera, yuv2rgb, picamera, pygame
from gui_button import *
from api_interface import *
import custom_events, config
from gui_screen5 import *
DEBUG = True

#some variables defined

def init():
    global menu

    menu = {}
#Defining rectangular buttons
    menu['btn1'] = Button('camera') #go back to navigation window
    menu['btn2'] = Button('1920,1080') #navigate left in the videos
    menu['btn3'] = Button('1280,720 ')#navigate right in the videos
    menu['btn4'] = Button('Settings')#Settings
    return None

def set_resolution(res):
    global camera
    config.camera_resolution = res 

def draw(screen, mouse, transparent = 0xFF):
    global menu

    x = 10
    y = 10
 
    height = 80 
    width = 60
    menu['btn1'].draw_rect(screen, mouse, (x,y,height,width), (x+10,y+20), transparent)
    menu['btn2'].draw_rect(screen, mouse, (x,y+160,height,width), (x+10,y+160+10), transparent)
    menu['btn3'].draw_rect(screen, mouse, (x+110,y+160,height,width), (x+110+20,y+160+10), transparent)
    menu['btn4'].draw_rect(screen, mouse, (x+220,y+160,height,width), (x+220+10,y+160+10), transparent)


def handle_event(mouse):
    global menu

#        return 2
    if menu['btn1'].obj.collidepoint(mouse):
        if DEBUG : print('button 1 clicked')
        pygame.event.post(custom_events.SWITCH_TO_CAMERA)
        config.camera_preview = True        
    elif menu['btn2'].obj.collidepoint(mouse):
        if DEBUG : print('button 2 clicked')
        set_resolution((1280,720))          
    elif menu['btn3'].obj.collidepoint(mouse):
        if DEBUG : print('button 3 clicked')
#        record()          
        set_resolution((1920,1080))          
    elif menu['btn4'].obj.collidepoint(mouse):
        if DEBUG : print('button 4 clicked')
             
    return None
