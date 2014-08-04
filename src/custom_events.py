import pygame
import config

SWITCH_TO_PLAYBACK = pygame.event.Event(pygame.USEREVENT + config.screen_ids['playback'] )
SWITCH_TO_NAVIGATION = pygame.event.Event(pygame.USEREVENT + config.screen_ids['navigation'] )
SWITCH_TO_CAMERA = pygame.event.Event(pygame.USEREVENT + config.screen_ids['camera'] )
SWITCH_TO_CAMERA_SETTINGS = pygame.event.Event(pygame.USEREVENT + config.screen_ids['camera_settings'] )
 
SWITCH_TO_POWER = pygame.event.Event(pygame.USEREVENT + config.screen_ids['power'] )
