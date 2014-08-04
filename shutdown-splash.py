#!/usr/bin/python

import pygame, os, time

def shutdown_splash():
   
   print("Initializing variables")
   #os.environ["TSLIB_TSDEVICE"] = "/dev/input/touchscreen"
   #os.environ["TSLIB_TSEVENTTYPE"] = "INPUT"
   #os.environ["TSLIB_CONFFILE"] = "/etc/ts.conf"
   #os.environ["TSLIB_CALIBFILE"] = "/etc/pointercal"
   os.environ["SDL_FBDEV"] = "/dev/fb1"
   #os.environ["SDL_MOUSEDEV"] = os.environ["TSLIB_TSDEVICE"]
   #os.environ["SDL_MOUSEDRV"] = "TSLIB"
   os.environ["SDL_VIDEODRIVER"] = "fbcon"
   #os.environ["SDL_AUDIODRIVER"] = "alsa"
      
   pygame.init()
     
   #size = (pygame.display.Info().current_w, pygame.display.Info().current_h)
   #print "Framebuffer size: %d x %d" % (size[0], size[1])
   
   screen=pygame.display.set_mode((320,240), pygame.FULLSCREEN)
      #self.screen.fill((0, 0, 0))
   
   pygame.mouse.set_visible(False)
   
   shutdown = pygame.image.load("./icons/shutdown-splash.png")

   screen.fill((0xFF,0x33,0x00)) #Background Color
   screen.blit(shutdown, (1,1))
   pygame.display.update()

   return None




shutdown_splash()
while True: pass
