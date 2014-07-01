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
    menu['btn1'] = Button('Playback') #Vol Up
    menu['btn2'] = Button('Power') #Vol Down
    menu['btn3'] = Button('Back')#Back
    menu['btn4'] = Button('Camera')#Play/Pause
    menu['btn5'] = Button('Select')#Enter
#defining Triangular Buttons
    menu['btn6'] = Button('')#'Button 6(Up)')
    menu['btn7'] = Button('')#'Button 7(Left)')
    menu['btn8'] = Button('')#'Button 8(Down)')
    menu['btn9'] = Button('')#'Button 9(Right)')            
    
    return None


def draw(screen, mouse):
    global menu
    
    menu['btn1'].draw_rect(screen, mouse, (0,0,80,80), (40,30))
    menu['btn2'].draw_rect(screen, mouse, (0,160,80,80), (40,190))
    menu['btn3'].draw_rect(screen, mouse, (240,160,80,80), (270,190))
    menu['btn4'].draw_rect(screen, mouse, (240,0,80,80), (270,30))
    menu['btn5'].draw_rect(screen, mouse, (120,80,80,80), (140,110))
                                    
    menu['btn6'].draw_triangle(screen, mouse, [[160,0],[120,70],[200,70]],(125,33))      #up 
    menu['btn7'].draw_triangle(screen, mouse, [[40,120],[110,80],[110,160]],(125,33))    #left
    menu['btn8'].draw_triangle(screen, mouse, [[160,240],[120,170],[200,170]],(125,33))  #down
    menu['btn9'].draw_triangle(screen, mouse, [[280,120],[210,80],[210,160]],(125,33))      #right 
          #btn.check_hover(mouse)
    return None


def handle_event(mouse):
    global menu

    if menu['btn1'].obj.collidepoint(mouse):
        print('button 1 clicked')
        return 2
            
    elif menu['btn2'].obj.collidepoint(mouse):
        print('button 2 clicked')
        playback_vol_dec()
                  
    elif menu['btn3'].obj.collidepoint(mouse):
        print('button 3 clicked')
        nav_back()
        
    elif menu['btn4'].obj.collidepoint(mouse):
        print('button 4 clicked')
#        playback_toggle_play()
            
    elif menu['btn5'].obj.collidepoint(mouse):
        print('button 5 clicked')
        nav_select()

    elif menu['btn6'].obj.collidepoint(mouse):
        print('button 6 clicked')
        nav_up()

    elif menu['btn7'].obj.collidepoint(mouse):
        print('button 7 clicked')
        nav_left()

    elif menu['btn8'].obj.collidepoint(mouse):
        print('button 8 clicked')
        nav_down()

    elif menu['btn9'].obj.collidepoint(mouse):
        print('button 9 clicked')
        nav_right()
    
    return 1
