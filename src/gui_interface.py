#Switches
INDEP = False #To test outside of XBMC
DEBUG = True
import pygame, os, time, sys, threading
import gui_screen1, gui_screen2, gui_screen3
import custom_events,config

def start_gui():
   
   global screen
   global clock
   global active_screen
   global camera_on   # for camera initialization deinitialization

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
#   drivers = [ 'fbcon', 'svgalib', 'directfb' ]
#   found = False
   pygame.init()
   if DEBUG:
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
#   pygame.font.init()
   # render the screen
   pygame.display.update()

   pygame.mouse.set_visible(False)
   #Initialising the screens
   gui_screen1.init()
   gui_screen2.init()
   gui_screen3.init()

   #setting display mode and resolution
   #screen = pygame.display.set_mode((320,240))
   clock = pygame.time.Clock()

   #Startup Animation
   startup_sequence()

   active_screen = 3 #Startup Menu

   camera_on = False

   return None


def update_gui():
   global screen
   global clock
   global active_screen
   global camera_on 
#   global t
   if not camera_on or not config.camera_preview:
       screen.fill((0xFF,0x33,0x00)) #Background Color
   else:
       gui_screen3.preview(screen)
   mouse = pygame.mouse.get_pos()

   if active_screen == 1 :   #active_screen =
      if camera_on:
#          t.join() 
          gui_screen3.deinit_camera()
          camera_on = False
          config.camera_preview = False
      gui_screen1.draw(screen, mouse)
   elif active_screen == 2 : #active_screen = 
      if camera_on:
#          t.join() 
          gui_screen3.deinit_camera()
          camera_on = False
          config.camera_preview = False
      gui_screen2.draw(screen, mouse)
   elif active_screen ==3:
      if not camera_on:
          gui_screen3.init_camera()  
#          t=threading.Thread(target = gui_screen3.preview)
#          t.start()
          camera_on = True
          config.camera_preview=True
      if config.recording: 
          gui_screen3.draw(screen, mouse, 50)      # to make the buttons transparent
#          print config.recording
      else:
          gui_screen3.draw(screen, mouse)
#          print config.recording

   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()
      if event.type == pygame.MOUSEBUTTONDOWN:
         mouse = pygame.mouse.get_pos()
         if active_screen == config.screen_ids['navigation'] :   #active_screen = 
            gui_screen1.handle_event(mouse)
         elif active_screen == config.screen_ids['playback'] :   #active_screen = 
            gui_screen2.handle_event(mouse)
         elif active_screen == config.screen_ids['camera'] :
            gui_screen3.handle_event(mouse)
      if event == custom_events.SWITCH_TO_PLAYBACK :
         print "Custom Event"
         active_screen = config.screen_ids['playback']
      if event == custom_events.SWITCH_TO_NAVIGATION :
         print "Custom Event"
         active_screen = config.screen_ids['navigation']
      if event == custom_events.SWITCH_TO_CAMERA :
         print "Custom Event"
         active_screen = config.screen_ids['camera']
              

   pygame.display.update()
   clock.tick(60)

   return None

def startup_sequence():
   pass
