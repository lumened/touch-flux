# This file defines the navigation screen.
# This requires the following procedures:
#  init()
#  draw()
#  handle_event()

from gui_button import *
from api_interface import *
import config, custom_events, api_projector
import pygame

def init():
    global menu

    menu = {}
#Defining rectangular buttons
    menu['btn1'] = Button('Shutdown', './icons/shutdown.png')
#    menu['btn2'] = Button('Restart', './icons/reboot.png')

    menu['btn3a'] = Button('Projector Off', './icons/projector-off.png')
    menu['btn3b'] = Button('Projector On', './icons/projector-on.png')

    menu['btn4a'] = Button('Charging Start', './icons/charging-start.png')
    menu['btn4b'] = Button('Charging Stop','./icons/charging-stop.png')
    #menu['btn6'] = Button('Forward', './icons/forward.png')#'Button 6(Up)')
    menu['btn7'] = Button('Nav', './icons/left.png')
    
    return None


def draw(screen, mouse):
    global menu
   
    x = 10
    y = 105
    button_height, button_width = (80,60) 

    menu['btn1'].draw_rect(screen, mouse, (x,y,button_height, button_width), (x,y))
#    menu['btn2'].draw_rect(screen, mouse, (x,y+70,button_height, button_width), (x,y+70))
   
#    menu['btn5'].draw_rect(screen, mouse, (x+220,y,button_height, button_width), (x+220,y))
#    menu['btn6'].draw_rect(screen, mouse, (x+220,y+70,button_height, button_width), (x+220,y+70))

    menu['btn7'].draw_rect(screen, mouse, (x,5,button_height, button_width), (x,5))
    
    font = pygame.font.Font(None, 22)
    screen.blit(font.render("Power Menu", 1, config.colors['white']), (140,15))

    #Live Update Area

    try : #If available, update
    #    speed = playback_speed()
        f = open("./src/battmonitor/data.txt", "r")
        percentage = int(f.read(3))
        plugged = f.read(1)
        if plugged == 'P': plugged_in = True
        elif plugged == 'U': plugged_in = False
        f.close()
        
        pygame.draw.rect(screen, config.colors['white'],(140,35,100,20))
        pygame.draw.rect(screen, config.colors['maroon'] , (142,36,percentage*96/100,18))
        pygame.draw.rect(screen, config.colors['white'],(240,40,6,10))
        font2 = pygame.font.Font(None, 18)
        screen.blit(font.render(str(percentage) + "%", 1, config.colors['white']), (280,35))
        if plugged_in: 
            screen.blit(pygame.image.load("./icons/plug-in.png"), (250, 35))

    #    time, total_time = playback_time()
    except: #Else, switch to screen 1
        if config.DEBUG: print("Data not available")
    #    config.manual_switch = False
    #    pygame.event.post(custom_events.SWITCH_TO_NAVIGATION)

#        switch_screen = True
#        return None

    #Battery Bar
    #pygame.draw.rect(screen, config.colors['white'],(140,25,140,20))
    #pygame.draw.rect(screen, config.colors['maroon'] , (142,27,percentage*136,18))

    #font2 = pygame.font.Font(None, 18)
    #screen.blit(font.render(str(percentage) + "%", 1, config.colors['white']), (140,25))
    
    ##Playback Status - Title + Time
    #font = pygame.font.Font(None, 22)
    #title = font.render(playback_title(), 1, config.colors['white'])
    #time = font.render(time + '/' + total_time, 1, config.colors['white'])
    #screen.blit(title, (10,15))
    #screen.blit(time, (10,40))



    ##Projector On/Off
    if config.projector : menu['btn3a'].draw_rect(screen, mouse, (x+110, y,button_height, button_width), (x+110, y))
    else: menu['btn3b'].draw_rect(screen, mouse, (x+110, y,button_height, button_width), (x+110, y))
    
    ##Charging On/Off
    if not config.charging : menu['btn4a'].draw_rect(screen, mouse, (x+220,y,button_height, button_width), (x+220,y))
    else : menu['btn4b'].draw_rect(screen, mouse, (x+220,y,button_height, button_width), (x+220,y))


    return None


def handle_event(mouse):
    global menu    
    
    print(config.projector)

    if menu['btn1'].obj.collidepoint(mouse):
        if config.DEBUG : print('Activate Shutdown')
        shutdown()
        sleep(10) #Still on
        from os import call
        call(["sudo","shutdown", "-h", "now"])
        
    #elif menu['btn2'].obj.collidepoint(mouse):
    #    if config.DEBUG : print('Reboot')

    elif (config.projector and menu['btn3a'].obj.collidepoint(mouse)) or (not config.projector and menu['btn3b'].obj.collidepoint(mouse)) :
        if config.DEBUG : print('Projector Power Toggle')
        #Toggle Projector State
        #config.projector = False if config.projector else True #Handled in toggle_projector()
        api_projector.toggle_projector()
        

    elif (not config.charging and menu['btn4a'].obj.collidepoint(mouse)) or (config.charging and menu['btn4b'].obj.collidepoint(mouse)) :
        if config.DEBUG : print('Charging Toggle')
        #Toggle Projector State
        config.charging = False if config.charging else True
            
#    elif menu['btn5'].obj.collidepoint(mouse):
#        if config.DEBUG : print('button 5 clicked')
#        playback_stop()
#        config.manual_switch = False
#        pygame.event.post(custom_events.SWITCH_TO_NAVIGATION)
#        return 1

#    elif menu['btn6'].obj.collidepoint(mouse):
#        if config.DEBUG : print('button 6 clicked')
#        playback_forward()

    elif menu['btn7'].obj.collidepoint(mouse):
        if config.DEBUG : print('Switch to Nav')
        pygame.event.post(custom_events.SWITCH_TO_NAVIGATION)
        config.manual_switch = True
    
    return None
