import pygame, os, time

from pygame import *

class Button:

   def __init__(self, text, icon = None):
      self.text = text
      self.is_hover = False
      self.default_color = (0xFF,0xE6,0xB3) #Buttons' Color
      self.hover_color = (0x88,0,0)
      self.font_color = (0xFF,0x33,0x00) #Text Color
      self.obj = None
      self.icon = icon
      
   def label(self):
      '''button label font'''
      font = pygame.font.Font(None, 20)
      return font.render(self.text, 1, self.font_color)
      
   def color(self):
      '''change color when hovering'''
      if self.is_hover:
         return self.hover_color
      else:
         return self.default_color
         
   def draw_rect(self, screen, mouse, rectcoord, labelcoord):
      '''create rect obj, draw, and change color based on input'''
      #self.obj  = pygame.draw.rect(screen, self.color(), rectcoord)
      self.obj  = self.AAfilledRoundedRect(screen, rectcoord, self.color())
      if self.icon is None : screen.blit(self.label(), labelcoord)
      else : 
         img = pygame.image.load(self.icon)
         screen.blit(img, labelcoord)
         
      #change color if mouse over button
      self.check_hover(mouse)
         
   def draw_triangle(self, screen, mouse, trianglecoord, labelcoord):
      self.obj = pygame.draw.polygon(screen, self.color(), trianglecoord)
      self.check_hover(mouse)

   def check_hover(self, mouse):
      '''adjust is_hover value based on mouse over button - to change hover color'''
      if self.obj.collidepoint(mouse):
         self.is_hover = True
      else:
         self.is_hover = False

   def AAfilledRoundedRect(self, surface, rect, color, radius=0.4):

      """
      AAfilledRoundedRect(surface,rect,color,radius=0.4)
      
      surface : destination
      rect    : rectangle
      color   : rgb or rgba
      radius  : 0 <= radius <= 1
      """
      
      rect         = Rect(rect)
      color        = Color(*color)
      alpha        = color.a
      color.a      = 0
      pos          = rect.topleft
      rect.topleft = 0,0
      rectangle    = Surface(rect.size,SRCALPHA)
      
      circle       = Surface([min(rect.size)*3]*2,SRCALPHA)
      draw.ellipse(circle,(0,0,0),circle.get_rect(),0)
      circle       = transform.smoothscale(circle,[int(min(rect.size)*radius)]*2)
      
      radius              = rectangle.blit(circle,(0,0))
      radius.bottomright  = rect.bottomright
      rectangle.blit(circle,radius)
      radius.topright     = rect.topright
      rectangle.blit(circle,radius)
      radius.bottomleft   = rect.bottomleft
      rectangle.blit(circle,radius)
      
      rectangle.fill((0,0,0),rect.inflate(-radius.w,0))
      rectangle.fill((0,0,0),rect.inflate(0,-radius.h))
      
      rectangle.fill(color,special_flags=BLEND_RGBA_MAX)
      rectangle.fill((255,255,255,alpha),special_flags=BLEND_RGBA_MIN)
      
      return surface.blit(rectangle,pos)

# End of Class Definition
