# This file defines the navigation screen.
# This requires the following procedures:
#  init()
#  draw()
#  handle_event()

from gui_button import *
from api_interface import *

def init():
    global menu

    menu = {}
#Defining rectangular buttons
    menu['btn1'] = Button('+') #Vol Up
    menu['btn2'] = Button('-') #Vol Down
    menu['btn3'] = Button('Play')#Back
    menu['btn4'] = Button('Back')#Play/Pause
    menu['btn5'] = Button('Stop')#Enter
    menu['btn6'] = Button('Forward')#'Button 6(Up)')
    menu['btn7'] = Button('Nav')#'Button 6(Up)')
    
    return None


def draw(screen, mouse):
    global menu
    
    x = 10
    y = 90
    button_height, button_width = (80,60) 

    menu['btn1'].draw_rect(screen, mouse, (x,y,button_height, button_width), (x,y))
    menu['btn2'].draw_rect(screen, mouse, (x,y+70,button_height, button_width), (x,y+80))
    menu['btn3'].draw_rect(screen, mouse, (x+110, y,button_height, button_width), (x+100, y))
    menu['btn4'].draw_rect(screen, mouse, (x+110,y+70,button_height, button_width), (x+100,y+80))
    menu['btn5'].draw_rect(screen, mouse, (x+220,y,button_height, button_width), (x+220,y))
    menu['btn6'].draw_rect(screen, mouse, (x+220,y+70,button_height, button_width), (x+220,y+70))

    menu['btn7'].draw_rect(screen, mouse, (x+220,10,button_height, button_width), (x+220,10))

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
#        playback_toggle_play()
            
    elif menu['btn5'].obj.collidepoint(mouse):
        print('button 5 clicked')
        playback_toggle_play()

    elif menu['btn6'].obj.collidepoint(mouse):
        print('button 6 clicked')


    elif menu['btn7'].obj.collidepoint(mouse):
        print('button 7 clicked')
        return 1
    
    return 2
