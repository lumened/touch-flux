import pygame, os 

os.environ["TSLIB_TSDEVICE"] = "/dev/input/event0"
os.environ["TSLIB_TSEVENTTYPE"] = "INPUT"
os.environ["TSLIB_CONFFILE"] = "/etc/ts.conf"
os.environ["TSLIB_CALIBFILE"] = "/etc/pointercal"
os.environ["SDL_FBDEV"] = "/dev/fb1"
os.environ["SDL_MOUSEDEV"] = os.environ["TSLIB_TSDEVICE"]
os.environ["SDL_MOUSEDRV"] = "TSLIB"
os.environ["SDL_VIDEODRIVER"] = "fbcon"
os.environ["SDL_AUDIODRIVER"] = "alsa"
size = (320,240)
screen=pygame.display.set_mode(size, pygame.FULLSCREEN)
screen.fill((255,255,255))
pygame.display.update()
while True:
    mouse = pygame.mouse.get_pos()
    if screen.collidepoint(mouse):
        print "hello"
    screen.fill((255,255,255))
    pygame.display.update()
