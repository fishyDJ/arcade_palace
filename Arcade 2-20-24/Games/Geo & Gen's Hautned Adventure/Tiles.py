# Map elements
import pygame, Images, random

class Tile(pygame.sprite.Sprite):
  def __init__(self, type, row, col):
    pygame.sprite.Sprite.__init__(self)
    self.type = type
    self.row = row
    self.col = col 

    if self.type == 'w':
      self.image = Images.wall
 
    elif self.type == 's':
      self.image = Images.trans

    elif self.type == 'b':
      if random.randint(0,1) == 1:
        self.image = Images.candy_green
      else: 
        self.image = Images.candy_orange
        
    elif self.type == 'c':
      self.image = Images.ghost

    else: # checks for errors in map list
      self.image = Images.trans
      print('RARRRRRR in map gen')
      self.kill()

    try:
      self.rect = self.image.get_rect()
      self.rect.x = col * 120
      self.rect.y = row * 120
    except: # If Error: dont crash 
      print('RAR')
      pass   

  def left(self, speed):
    self.rect.x += speed
  def right(self, speed):
    self.rect.x -= speed
  def up(self, speed):
    self.rect.y += speed
  def down(self, speed):
    self.rect.y -= speed
    