#Switches
#INDEP = False #To test outside of XBMC
DEBUG = True  #To enable debugging messages

import pygame, os, time, sys
from gui_button import *
from api_interface import *

def start_gui():
   
   global screen
   global clock
   global btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9

   os.environ["TSLIB_TSDEVICE"] = "/dev/input/event0"
   os.environ["TSLIB_TSEVENTTYPE"] = "INPUT"
   os.environ["TSLIB_CONFFILE"] = "/etc/ts.conf"
   os.environ["TSLIB_CALIBFILE"] = "/etc/pointercal"
   os.environ["SDL_FBDEV"] = "/dev/fb1"
   os.environ["SDL_MOUSEDEV"] = os.environ["TSLIB_TSDEVICE"]
   os.environ["SDL_MOUSEDRV"] = "TSLIB"
   os.environ["SDL_VIDEODRIVER"] = "fbcon"
   os.environ["SDL_AUDIODRIVER"] = "alsa"
   pygame.init()
   print __name__
   
   disp_no = os.getenv("DISPLAY")
   if disp_no:
      print "I'm running under X display = {0}".format(disp_no)
      
      # Start with fbcon since directfb hangs with composite output
   drivers = [ 'fbcon', 'svgalib', 'directfb']
   found = False
#   for driver in drivers:
      # Make sure that SDL_VIDEODRIVER is set
#      if not os.getenv('SDL_VIDEODRIVER'):
#         os.putenv('SDL_VIDEODRIVER', driver)
#         try:
#            pygame.display.init()
#            print driver
#         except pygame.error:
#            print 'Driver: {0} failed.'.format(driver)
#            continue
#         found = True
#         break
#   if not found:
#      raise Exception('No suitable video driver found!')
   pygame.init()
   print os.getenv('SDL_VIDEODRIVER')
   size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
   print "Framebuffer size: %d x %d" % (size[0], size[1])
   
      #No self in this scope??
      #self.screen = 
   screen=pygame.display.set_mode(size, pygame.FULLSCREEN)
      #self.screen.fill((0, 0, 0))
      # Initialise font support
   pygame.font.init()
 # render the screen
   pygame.display.update()

#Defining rectangular buttons
   btn1 = Button('+') #Vol Up
   btn2 = Button('-') #Vol Down
   btn3 = Button('Back')#Back
   btn4 = Button('Play')#Play/Pause
   btn5 = Button('Select')#Enter
#defining Triangular Buttons
   btn6 = Button('')#'Button 6(Up)')
   btn7 = Button('')#'Button 7(Left)')
   btn8 = Button('')#'Button 8(Down)')
   btn9 = Button('')#'Button 9(Right)')            

   #setting display mode and resolution
#   screen = pygame.display.set_mode((320,240))
   clock = pygame.time.Clock()

def update_gui():
   global screen
   global clock
   global btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9
   global run

   screen.fill((255,255,255))
   mouse = pygame.mouse.get_pos()
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
         mouse = pygame.mouse.get_pos()
         if btn1.obj.collidepoint(mouse):
            #Increase Volume Handler
            print('button 1 clicked')
#            playback_vol_inc()
            
         elif btn2.obj.collidepoint(mouse):
            #Decrease Volume Handler
            print('button 2 clicked')
            playback_vol_dec()
                  
         elif btn3.obj.collidepoint(mouse):
            print('button 3 clicked')
            nav_back()
            
         if btn4.obj.collidepoint(mouse):
            print('button 4 clicked')
            playback_toggle_play()

         if btn5.obj.collidepoint(mouse):
            print('button 5 clicked')
            nav_select()

         if btn6.obj.collidepoint(mouse):
            print('button 6 clicked')
            nav_up()

         if btn7.obj.collidepoint(mouse):
            print('button 7 clicked')
            nav_left()

         if btn8.obj.collidepoint(mouse):
            print('button 8 clicked')
            nav_down()

         if btn9.obj.collidepoint(mouse):
            print('button 9 clicked')
            nav_right()
                                    
   btn1.draw_rect(screen, mouse, (0,0,80,80), (40,30))
   btn2.draw_rect(screen, mouse, (0,160,80,80), (40,190))
   btn3.draw_rect(screen, mouse, (240,160,80,80), (270,190))
   btn4.draw_rect(screen, mouse, (240,0,80,80), (270,30))
   btn5.draw_rect(screen, mouse, (120,80,80,80), (140,110))
                                    
   btn6.draw_triangle(screen, mouse, [[160,0],[120,70],[200,70]],(125,33))      #up 
   btn7.draw_triangle(screen, mouse, [[40,120],[110,80],[110,160]],(125,33))    #left
   btn8.draw_triangle(screen, mouse, [[160,240],[120,170],[200,170]],(125,33))  #down
   btn9.draw_triangle(screen, mouse, [[280,120],[210,80],[210,160]],(125,33))      #right 
          #btn.check_hover(mouse)
      
   pygame.display.update()
   clock.tick(60)

