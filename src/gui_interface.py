import pygame, os, time, sys, threading, platform
import gui_screen1, gui_screen2, gui_screen3, gui_screen4, gui_screen5, api_camera
import custom_events,config

def start_gui():
   
   global INDEP
   global screen
   global clock
   global active_screen
   global camera_on   # for camera initialization deinitialization


   for x in platform.uname():
      if 'raspbmc' in x: 
         print("Starting in RaspBMC")
         INDEP = False #To test outside of XBMC
         break
      else : INDEP = True

   print(INDEP)
   if not INDEP :
      print("Initializing variables")
      os.environ["TSLIB_TSDEVICE"] = "/dev/input/touchscreen"
      os.environ["TSLIB_TSEVENTTYPE"] = "INPUT"
      os.environ["TSLIB_CONFFILE"] = "/etc/ts.conf"
      os.environ["TSLIB_CALIBFILE"] = "/etc/pointercal"
      os.environ["SDL_FBDEV"] = "/dev/fb1"
      os.environ["SDL_MOUSEDEV"] = os.environ["TSLIB_TSDEVICE"]
      os.environ["SDL_MOUSEDRV"] = "TSLIB"
      os.environ["SDL_VIDEODRIVER"] = "fbcon"
      os.environ["SDL_AUDIODRIVER"] = "alsa"
      
   pygame.mixer.quit()
   pygame.init()
   pygame.mixer.quit()
   pygame.mouse.set_visible(False)
   
   print __name__
      
   disp_no = os.getenv("DISPLAY")
   if disp_no: print "I'm running under X display = {0}".format(disp_no)
      
   pygame.init()
   pygame.mixer.quit()
   if config.DEBUG:
       print os.getenv('SDL_VIDEODRIVER')
   if INDEP:
      size = (320,240)
   else:
      size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
   if config.DEBUG:
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
   gui_screen4.init()
   gui_screen5.init()

#   startup_sequence()

   #setting display mode and resolution
   #screen = pygame.display.set_mode((320,240))
   clock = pygame.time.Clock()

   #Startup Animation
#   startup_sequence()

   #active_screen = 3 #Startup Menu

   camera_on = False
#   startup_sequence()
#   pygame.mixer.quit()
   pygame.event.set_blocked(pygame.MOUSEMOTION)
   active_screen = 1 #Startup Menu

   return None


def update_gui():
   global screen
   global clock
   global active_screen
   global camera_on 
   if camera_on and config.camera_preview:
       api_camera.preview(screen)
   else:
       screen.fill((0xFF,0x33,0x00)) #Background Color
   mouse = pygame.mouse.get_pos()

   if active_screen == 1 :
      if camera_on:
#          t.join() 
          api_camera.deinit_camera()
          #api_audio.deinit_audio()
          camera_on = False
          config.camera_preview = False
          screen.fill((0xFF,0x33,0x00)) #Background Color
      gui_screen1.draw(screen, mouse)
   elif active_screen == 2 : #active_screen = 
      if camera_on:
#          t.join() 
          api_camera.deinit_camera()
          #api_audio.deinit_audio()
          camera_on = False
          config.camera_preview = False
      gui_screen2.draw(screen, mouse)
   elif active_screen == 3:
      if not camera_on:
          #api_audio.init_audio()
          api_camera.init_camera()  
          camera_on = True
          config.camera_preview = True
#      elif not camera_preview:
#          camera_preview = on
      if config.recording: 
          gui_screen3.draw(screen, mouse, 50)      # to make the buttons transparent
      else:
          gui_screen3.draw(screen, mouse)
   elif active_screen == 4 :
      if camera_on:
#          t.join() 
          api_camera.deinit_camera()
          #api_audio.deinit_audio()
          camera_on = False
          config.camera_preview = False
      gui_screen4.draw(screen, mouse)

   elif active_screen == 5:
      if camera_on:
#          t.join() 
          api_camera.deinit_camera()
          #api_audio.deinit_audio()
          camera_on = False
          config.camera_preview = False
#      if config.camera_preview:
#          config.camera_preview = False
      gui_screen5.draw(screen, mouse) 

#   if active_screen == 1 :  
#      gui_screen1.draw(screen, mouse)
#   elif active_screen == 2 : 
#      gui_screen2.draw(screen, mouse)
#   elif active_screen == 4:
#      gui_screen4.draw(screen, mouse)


   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         sys.exit()

      if event.type == pygame.MOUSEBUTTONDOWN:
         mouse = pygame.mouse.get_pos()
         if active_screen == config.screen_ids['navigation'] :   
            gui_screen1.handle_event(mouse)
         elif active_screen == config.screen_ids['playback'] :   #active_screen = 
            gui_screen2.handle_event(mouse)
         elif active_screen == config.screen_ids['camera'] :
            gui_screen3.handle_event(mouse)
         elif active_screen == config.screen_ids['camera_settings'] :
            gui_screen5.handle_event(mouse)
         elif active_screen == config.screen_ids['playback'] : 
            gui_screen2.handle_event(mouse)
         elif active_screen == config.screen_ids['power'] : 
            gui_screen4.handle_event(mouse)

      if event == custom_events.SWITCH_TO_PLAYBACK :
         if config.DEBUG : print("Custom Event")
         config.update_screen = True
         active_screen = config.screen_ids['playback']

      if event == custom_events.SWITCH_TO_NAVIGATION :
         if config.DEBUG : print "Custom Event (Navigation)"
         config.update_screen = True
         active_screen = config.screen_ids['navigation']
      if event == custom_events.SWITCH_TO_CAMERA :
         if config.DEBUG : print "Custom Event(Camera)"
         config.update_screen = True
         active_screen = config.screen_ids['camera']
      if event == custom_events.SWITCH_TO_CAMERA_SETTINGS :
         if config.DEBUG : print "Custom Event(camera settings)"
         config.update_screen = True
         active_screen = config.screen_ids['camera_settings']
      if event == custom_events.SWITCH_TO_POWER :
         if config.DEBUG : print "Custom Event(power)"
         config.update_screen = True
         active_screen = config.screen_ids['power']            

#   import cProfile
#   cProfile.run('pygame.display.update()')
#   pygame.display.update()
   clock.tick(4) #Controls FPS
#   pygame.time.wait(50)

   return None


def startup_sequence():
   
   global screen
   logo = pygame.image.load("./icons/lumened.png")
   colorkey = [0, 0, 0]
   logo.set_colorkey(colorkey)
   logo.set_alpha(None)
   logo = logo.convert()

   for i in range(1,40):
      screen.fill((0xFF,0x33,0x00)) #Background Color
      logo.set_alpha(255*i/40)
      screen.blit(logo, (1,1))
      pygame.display.update()
      time.sleep(0.1)

#   logo.set_alpha(None)
#   logo = logo.convert()

   for j in range(10,1,-1):
      screen.fill((0xFF,0x33,0x00)) #Background Color
      logo.set_alpha(255*j/10)
      screen.blit(logo, (1,1))
      pygame.display.update()
      time.sleep(0.1)
      
#   for i in range(20,1):
#      screen.fill((0xFF,0x33,0x00)) #Background Color
#      logo.set_alpha(255*i/20)
#      screen.blit(logo, (1,1))
#      pygame.display.update()
#      time.sleep(0.2)

   screen.fill((0xFF,0x33,0x00)) #Background Color
#   time.sleep(5)
   return None




