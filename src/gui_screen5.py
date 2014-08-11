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

#some variables defined

def init():
    global menu

    menu = {}
#Defining rectangular buttons
    menu['btn1'] = Button('camera' , './icons/camera.png') #go back to navigation window
    menu['btn2'] = Button('1280,720' , './icons/720p-icon.png') #navigate left in the videos
    menu['btn3'] = Button('640,480 ' , './icons/480p-icon.png')#navigate right in the videos
    menu['btn4'] = Button('480,360' , './icons/360p-icon.png')#Settings
    return None

def set_resolution(res):
    global camera
    config.mode = res 

def draw(screen, mouse, transparent = 0xFF):
    global menu

    x = 10
    y = 10
 
    height = 80 
    width = 60
    menu['btn1'].draw_rect(screen, mouse, (x,y,height,width), (x,y), transparent)
    menu['btn2'].draw_rect(screen, mouse, (x,y+160,height,width), (x,y+160), transparent)
    menu['btn3'].draw_rect(screen, mouse, (x+110,y+160,height,width), (x+110,y+160), transparent)
    menu['btn4'].draw_rect(screen, mouse, (x+220,y+160,height,width), (x+220,y+160), transparent)

    pygame.display.update()
    config.update_screen = False
    return None

def handle_event(mouse):
    global menu

#        return 2
    if menu['btn1'].obj.collidepoint(mouse):
        if config.DEBUG : print('button 1(screen 5) clicked')
        pygame.event.post(custom_events.SWITCH_TO_CAMERA)
        config.camera_preview = True        
    elif menu['btn2'].obj.collidepoint(mouse):
        if config.DEBUG : print('button 2 clicked')
        set_resolution(0)          
    elif menu['btn3'].obj.collidepoint(mouse):
        if config.DEBUG : print('button 3 clicked')
        set_resolution(1)          
#        record()          
        set_resolution((1920,1080))          
    elif menu['btn4'].obj.collidepoint(mouse):
        if config.DEBUG : print('button 4 clicked')
        set_resolution(2)          
             
    return None
