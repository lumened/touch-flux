# This file defines the navigation screen. This requires the following procedures:
#  init()
#  draw()
#  handle_event()
import datetime
import atexit, io, os, yuv2rgb, picamera, pygame
from gui_button import *
from api_interface import *
import custom_events, api_camera

DEBUG = True

#some variables defined

def init():
    global menu

    menu = {}
#Defining rectangular buttons
    menu['btn1'] = Button('navigation' ,'./icons/left.png') #go back to navigation window
    menu['btn2'] = Button('left' ,'./icons/left-navigate.png' ) #navigate left in the videos
    menu['btn3'] = Button('right' ,'./icons/right-navigate.png')#navigate right in the videos
    menu['btn4'] = Button('Settings' ,'./icons/icon-settings.png')#Settings
    menu['surface'] = Button(' ')
    return None


def render_text(screen, text, coord):
    myfont = pygame.font.SysFont("monospace", 15)
    label = myfont.render(text, 1, config.colors['white'])
    screen.blit(label, coord)
 
def display_video_info(screen):
#    global count
#    date = time.strftime("%d-%m-%Y")
    full_path = "video" + "%03d"%config.count
    files = os.listdir(config.path)
#    print full_path
    for item in files:
#         print "for"
         if item.find(full_path)!= -1:
#             print item
             render_text(screen, item, (50,120))

def display_video_time(screen):
    # render text
    current_time = datetime.datetime.now()
#    elapsed_time = str((current_time.hour - start_time.hour)%24) + ":" + str((current_time.minute- start_time.minute)%60) + ":" +  str((current_time.second - start_time.second)%60)
    elapsed_time = str(current_time - config.start_time)
    elapsed_time = elapsed_time.rpartition(".")[0]            # to remove the milliseconds
    render_text(screen, elapsed_time, (130,20))

def draw(screen, mouse, transparent = 0xFF):
    global menu

    x = 10
    y = 10
 
    height = 80 
    width = 60
    menu['surface'].draw_rect(screen, mouse, (0,0,240,320), (0,0),0)    #surface not becoming transparent
    menu['btn1'].draw_rect(screen, mouse, (x,y,height,width), (x,y), transparent)
    menu['btn2'].draw_rect(screen, mouse, (x,y+160,height,width), (x,y+160), transparent)
    menu['btn3'].draw_rect(screen, mouse, (x+220,y+160,height,width), (x+220,y+160), transparent)
    menu['btn4'].draw_rect(screen, mouse, (x+220,y,height,width), (x+220,y), transparent)
#    if config.recording:
#         display_video_time(screen)
          #btn.check_hover(mouse)
    if not config.camera_preview:
         display_video_info(screen)
    return None


def handle_event(mouse):
    global menu

#        return 2
    if menu['btn1'].obj.collidepoint(mouse) and config.camera_preview:
        if DEBUG : print('button 1 clicked')
        pygame.event.post(custom_events.SWITCH_TO_NAVIGATION)
    elif menu['btn1'].obj.collidepoint(mouse) and not config.camera_preview:
        if DEBUG : print('button 1 clicked')
        config.camera_preview = True           
    elif menu['btn2'].obj.collidepoint(mouse):
        if DEBUG : print('button 2 clicked')
        api_camera.navigation(-1)          
    elif menu['btn3'].obj.collidepoint(mouse) and config.camera_preview:
        if DEBUG : print('button 3 clicked')
#        record()          
        api_camera.navigation(0)
    elif menu['btn3'].obj.collidepoint(mouse) and not config.camera_preview:
        if DEBUG : print('button 3 clicked')
#        record()          
        api_camera.navigation(1)
    elif menu['btn4'].obj.collidepoint(mouse):
        if DEBUG : print('button 4 clicked')
        pygame.event.post(custom_events.SWITCH_TO_CAMERA_SETTINGS)        
        config.camera_preview = False
    elif menu['surface'].obj.collidepoint(mouse) and config.camera_preview:
        if DEBUG : print('surface clicked recording')
        api_camera.record()
        #api_audio.record()
    elif menu['surface'].obj.collidepoint(mouse) and not config.camera_preview:
        if DEBUG : print('surface clicked and video started')
 #       mplayer
    return None
