# This file defines the navigation screen.
# This requires the following procedures:
#  init()
#  draw()
#1;3202;0c  handle_event()

from gui_button import *
from api_interface import *
import config, custom_events
import pygame

def init():
    global menu, font

    menu = {}
#Defining rectangular buttons
    menu['btn1'] = Button('+', './icons/vol-up.png') #Vol Up
    menu['btn2'] = Button('-', './icons/vol-down.png') #Vol Down

    menu['btn3'] = Button('Play', './icons/play.png')
    menu['btn8'] = Button('Pause', './icons/pause.png')

    menu['btn4'] = Button('Rewind', './icons/rewind.png')
    menu['btn5'] = Button('Stop','./icons/stop.png')#Stop
    menu['btn6'] = Button('Forward', './icons/forward.png')
    menu['btn7'] = Button('Back', './icons/back.png')

    font = pygame.font.Font(None, 22)
    
    return None


def draw(screen, mouse):
    global menu,speed,font
#    global switch_screen
#    switch_screen = False

    x = 10
    y = 105
    button_height, button_width = (80,60) 
        
    if config.update_screen:
        
        menu['btn1'].draw_rect(screen, mouse, (x,y,button_height, button_width), (x,y))
        menu['btn2'].draw_rect(screen, mouse, (x,y+70,button_height, button_width), (x,y+70))
        
        menu['btn4'].draw_rect(screen, mouse, (x+110,y+70,button_height, button_width), (x+110,y+70))
        menu['btn5'].draw_rect(screen, mouse, (x+220,y,button_height, button_width), (x+220,y))
        menu['btn6'].draw_rect(screen, mouse, (x+220,y+70,button_height, button_width), (x+220,y+70))
        
        menu['btn7'].draw_rect(screen, mouse, (x,5,button_height, button_width), (x,5))
        title = font.render(playback_title(), 1, config.colors['white'])
        screen.blit(title, (100+10,15))

        #pygame.display.update()
#        config.update_screen = False #Dont redraw till switch       
    
    #Live Update Area

    try : #If available, update
        speed = playback_speed()
        percentage = playback_percentage()/100
        time, total_time = playback_time()
    except: #Else, switch to screen 1
        config.manual_switch = False
        pygame.event.post(custom_events.SWITCH_TO_NAVIGATION)

#        switch_screen = True
        return None

    ##Progressbar
    pygame.draw.rect(screen, config.colors['white'],(5,70,310,25))
    pygame.draw.rect(screen, config.colors['maroon'] , (7,72,percentage*306,21))
    
    ##Playback Status - Title + Time
    #title = font.render(playback_title(), 1, config.colors['white'])
    time = font.render(time + '/' + total_time, 1, config.colors['white'])
#    screen.blit(title, (100+10,15))
    screen.blit(time, (100+10,40))

    ##Play Pause Buttons : Require live update due to navigation options
    if speed==0 : menu['btn3'].draw_rect(screen, mouse, (x+110, y,button_height, button_width), (x+110, y))
    else: menu['btn8'].draw_rect(screen, mouse, (x+110, y,button_height, button_width), (x+110, y))

    if config.update_screen: 
        pygame.display.update()
        config.update_screen = False
    else: 
        pygame.display.update((110,40,200,30)) #Live Update Area
        pygame.display.update((5,70,310,25 )) #Progress Bar
        pygame.display.update((x+110,y,button_height, button_width)) #Play/Pause Button

    return None


def handle_event(mouse):
    global menu, speed
#    global switch_screen

#    if switch_screen : return 1
    
    if menu['btn1'].obj.collidepoint(mouse):
        if config.DEBUG : print('button 1 clicked')
        playback_vol_inc()
            
    elif menu['btn2'].obj.collidepoint(mouse):
        if config.DEBUG : print('button 2 clicked')
        playback_vol_dec()
                  
    elif (speed == 0 and menu['btn3'].obj.collidepoint(mouse)):
        if config.DEBUG : print('button 3 clicked')
        playback_toggle_play()

    elif (speed != 0 and menu['btn8'].obj.collidepoint(mouse)):
        if config.DEBUG : print('button 3 clicked')
        playback_toggle_play()
        
    elif menu['btn4'].obj.collidepoint(mouse):
        if config.DEBUG : print('button 4 clicked')
        playback_rewind()
            
    elif menu['btn5'].obj.collidepoint(mouse):
        if config.DEBUG : print('button 5 clicked')
        playback_stop()
        config.manual_switch = False
        pygame.event.post(custom_events.SWITCH_TO_NAVIGATION)
#        return 1

    elif menu['btn6'].obj.collidepoint(mouse):
        if config.DEBUG : print('button 6 clicked')
        playback_forward()

    elif menu['btn7'].obj.collidepoint(mouse):
        if config.DEBUG : print('button 7 clicked')
        pygame.event.post(custom_events.SWITCH_TO_NAVIGATION)
        config.manual_switch = True
#        return 1
    
    return None
