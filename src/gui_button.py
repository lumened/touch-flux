import pygame, os, time

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
      self.obj  = pygame.draw.rect(screen, self.color(), rectcoord)
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
# End of Class Definition
