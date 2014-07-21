# This file defines the navigation screen.
# This requires the following procedures:
#  init()
#  draw()
#  handle_event()
import time, pygame

from gui_button import *
from api_interface import *
import config, custom_events


def init():
    global menu

    menu = {}
#Defining rectangular buttons
    menu['btn1'] = Button('Playback', './icons/playback.png') #Vol Up
    menu['btn2'] = Button('Power', './icons/power.png') #Vol Down
    menu['btn3'] = Button('Back', './icons/back.png')#Back
    menu['btn4'] = Button('Camera', './icons/camera.png')#Play/Pause
    menu['btn5'] = Button('Select', './icons/select.png')#Enter
#defining Triangular Buttons
    menu['btn6'] = Button('')#'Button 6(Up)')
    menu['btn7'] = Button('')#'Button 7(Left)')
    menu['btn8'] = Button('')#'Button 8(Down)')
    menu['btn9'] = Button('')#'Button 9(Right)')            
    
    return None


def draw(screen, mouse):
    global menu

    if not config.manual_switch and playback_find_player() is not None :
        pygame.event.post(custom_events.SWITCH_TO_PLAYBACK)
        return None

    if not config.update_screen: return None

    x = 10
    y = 10
    
    height = 80 
    width = 60
        
    menu['btn1'].draw_rect(screen, mouse, (x,y,height,width), (x,y))
    menu['btn2'].draw_rect(screen, mouse, (x,y+160,height,width), (x,y+160))
    menu['btn3'].draw_rect(screen, mouse, (x+220,y+160,height,width), (x+220,y+160))
    menu['btn4'].draw_rect(screen, mouse, (x+220,y,height,width), (x+220,y))
    menu['btn5'].draw_rect(screen, mouse, (120,80,80,80), (120,80))
                                    
    menu['btn6'].draw_triangle(screen, mouse, [[160,0],[120,70],[200,70]],(125,33))      #up 
    menu['btn7'].draw_triangle(screen, mouse, [[40,120],[110,80],[110,160]],(125,33))    #left
    menu['btn8'].draw_triangle(screen, mouse, [[160,240],[120,170],[200,170]],(125,33))  #down
    menu['btn9'].draw_triangle(screen, mouse, [[280,120],[210,80],[210,160]],(125,33))      #right 
          #btn.check_hover(mouse)

    pygame.display.update()
    config.update_screen = False #Dont redraw till switch
    return None


def handle_event(mouse):
    global menu

#    if playback_find_player() is not None :
#        pygame.event.post(custom_events.SWITCH_TO_PLAYBACK)

    if menu['btn1'].obj.collidepoint(mouse):
        if config.DEBUG : print('button 1 clicked')
        pygame.event.post(custom_events.SWITCH_TO_PLAYBACK)

            
    elif menu['btn2'].obj.collidepoint(mouse):
        if config.DEBUG : print('button 2 clicked')
        pygame.event.post(custom_events.SWITCH_TO_POWER)
                  
    elif menu['btn3'].obj.collidepoint(mouse):
        if config.DEBUG : print('button 3 clicked')
        nav_back()
        
    elif menu['btn4'].obj.collidepoint(mouse):
        if config.DEBUG : print('button 4 clicked')
            
    elif menu['btn5'].obj.collidepoint(mouse):
        if config.DEBUG : print('button 5 clicked')
        nav_select()
#        time.sleep(0.50)
#        if playback_find_player() is not None:
#            pygame.event.post(custom_events.SWITCH_TO_PLAYBACK)
#            return 2

    elif menu['btn6'].obj.collidepoint(mouse):
        if config.DEBUG : print('button 6 clicked')
        nav_up()

    elif menu['btn7'].obj.collidepoint(mouse):
        if config.DEBUG : print('button 7 clicked')
        nav_left()

    elif menu['btn8'].obj.collidepoint(mouse):
        if config.DEBUG : print('button 8 clicked')
        nav_down()

    elif menu['btn9'].obj.collidepoint(mouse):
        if config.DEBUG : print('button 9 clicked')
        nav_right()
    
    return None
