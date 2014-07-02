# This file defines the navigation screen.
# This requires the following procedures:
#  init()
#  draw()
#  handle_event()

from gui_button import *
from api_interface import *
import pygame

def init():
    global menu

    menu = {}
#Defining rectangular buttons
    menu['btn1'] = Button('+', './icons/vol-up.png') #Vol Up
    menu['btn2'] = Button('-', './icons/vol-down.png') #Vol Down
    menu['btn3'] = Button('Play', './icons/play.png')#Back
    menu['btn4'] = Button('Back', './icons/rewind.png')#Play/Pause
    menu['btn5'] = Button('Stop','./icons/stop.png')#Stop
    menu['btn6'] = Button('Forward', './icons/forward.png')#'Button 6(Up)')
    menu['btn7'] = Button('Nav', './icons/right.png')#Button 6(Up)')
    
    return None


def draw(screen, mouse):
    global menu
    
    x = 10
    y = 105
    button_height, button_width = (80,60) 
    
    colors = {'orange':(0xFF,0x33,0x00), 'white':(0xFF,0xE6,0xB3), 'maroon':(0x88,0x00,0x00)}


    menu['btn1'].draw_rect(screen, mouse, (x,y,button_height, button_width), (x,y))
    menu['btn2'].draw_rect(screen, mouse, (x,y+70,button_height, button_width), (x,y+70))
    menu['btn3'].draw_rect(screen, mouse, (x+110, y,button_height, button_width), (x+110, y))
    menu['btn4'].draw_rect(screen, mouse, (x+110,y+70,button_height, button_width), (x+110,y+70))
    menu['btn5'].draw_rect(screen, mouse, (x+220,y,button_height, button_width), (x+220,y))
    menu['btn6'].draw_rect(screen, mouse, (x+220,y+70,button_height, button_width), (x+220,y+70))

    menu['btn7'].draw_rect(screen, mouse, (x+220,5,button_height, button_width), (x+220,5))
    
    #Live Update Area

    ##Progressbar
    pygame.draw.rect(screen, colors['white'],(5,70,310,25))
    percentage = playback_percentage()/100
    pygame.draw.rect(screen, colors['maroon'] , (7,72,percentage*306,21))
    
    ##Playback Status - Title + Time
    font = pygame.font.Font(None, 20)
    title = font.render(playback_title(), 1, (255,255,255))
    time, total_time = playback_time()
    time = font.render(time + '/' + total_time, 1, (255,255,255))
    screen.blit(title, (10,20))
    screen.blit(time, (10,40))

    return None


def handle_event(mouse):
    global menu

    if menu['btn1'].obj.collidepoint(mouse):
        print('button 1 clicked')
        playback_vol_inc()
            
    elif menu['btn2'].obj.collidepoint(mouse):
        print('button 2 clicked')
        playback_vol_dec()
                  
    elif menu['btn3'].obj.collidepoint(mouse):
        print('button 3 clicked')
        playback_toggle_play()
        
    elif menu['btn4'].obj.collidepoint(mouse):
        print('button 4 clicked')
        playback_rewind()
            
    elif menu['btn5'].obj.collidepoint(mouse):
        print('button 5 clicked')
        playback_stop()
        return 1

    elif menu['btn6'].obj.collidepoint(mouse):
        print('button 6 clicked')
        playback_forward()

    elif menu['btn7'].obj.collidepoint(mouse):
        print('button 7 clicked')
        return 1
    
    return 2
