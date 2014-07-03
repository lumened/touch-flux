import pygame
import config

SWITCH_TO_PLAYBACK = pygame.event.Event(pygame.USEREVENT + config.screen_ids['playback'] )
SWITCH_TO_NAVIGATION = pygame.event.Event(pygame.USEREVENT + config.screen_ids['navigation'] )
SWITCH_TO_CAMERA = pygame.event.Event(pygame.USEREVENT + config.screen_ids['camera'] )
