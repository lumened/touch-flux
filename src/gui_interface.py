#Switches
INDEP = True #To test outside of XBMC

import pygame, os, time, sys
import gui_screen1

def start_gui():
   
   global screen
   global clock
   
   if not INDEP :
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
   if disp_no: print "I'm running under X display = {0}".format(disp_no)
      
   # Start with fbcon since directfb hangs with composite output
   drivers = [ 'fbcon', 'svgalib', 'directfb' ]
   found = False
   pygame.init()
   print os.getenv('SDL_VIDEODRIVER')
   if INDEP:
      size = (320,240)
   else:
      size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
   print "Framebuffer size: %d x %d" % (size[0], size[1])
   
   if INDEP:
      screen=pygame.display.set_mode(size, pygame.RESIZABLE)
   else:
      screen=pygame.display.set_mode(size, pygame.FULLSCREEN)
      #self.screen.fill((0, 0, 0))
   
   #Initialise font support
   pygame.font.init()
   # render the screen
   pygame.display.update()

   #Initialising the screens
   gui_screen1.init()

   #setting display mode and resolution
   #screen = pygame.display.set_mode((320,240))
   clock = pygame.time.Clock()

   return None


def update_gui():
   global screen
   global clock

   screen.fill((255,255,255))
   mouse = pygame.mouse.get_pos()
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
         mouse = pygame.mouse.get_pos()
         gui_screen1.handle_event(mouse)
              
   gui_screen1.draw(screen, mouse)

   pygame.display.update()
   clock.tick(60)

   return None
