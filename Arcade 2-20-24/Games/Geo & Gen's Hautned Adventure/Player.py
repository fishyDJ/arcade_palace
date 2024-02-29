
# Player
import pygame, Images

class Player(pygame.sprite.Sprite):
  def __init__(self, collide_tiles, all_tiles, candy, screen_width, screen_height):
    pygame.sprite.Sprite.__init__(self)
    self.collide_tiles = collide_tiles
    self.all_tiles = all_tiles
    self.candy = candy
    self.image = Images.player_still
    self.rect = self.image.get_rect()
    self.rect.x = screen_width//2
    self.rect.y = screen_height//2

    # Animation
    self.animation_timer = 5
    self.animation_itteration = -1
    self.animation_right = [None, Images.player_right1, Images.player_right2]
    self.animation_left = [None, Images.player_left1, Images.player_left2]
    self.animation_up = [None, Images.player_up1, Images.player_up2]
    self.animation_down = [None, Images.player_down1, Images.player_down2]
    self.animation_still = [Images.player_still_left, Images.player_still_right, Images.player_still_up, Images.player_still_down]
    self.last_direction = 1   # 1 = left, 2 = right, 3 = up, 4 = down
    self.did_animate = False

    # Movement 
    self.left = False
    self.right = False
    self.up = False
    self.down = False
    self.speed = 5

  def movestart(self, direction): # 1 = left, 2 = right, 3 = up, 4 = down
    pygame.sprite.Sprite.__init__(self)
    if direction == 1: # Direction Recognition  
      self.left = True
    elif direction == 2:
      self.right = True
    elif direction == 3:
      self.up = True
    elif direction == 4:
      self.down = True

  def movestop(self, direction): # stop moving (key up)
    if direction == 1: # Direction Recognition  
      self.left = False
    elif direction == 2:
      self.right = False
    elif direction == 3:
      self.up = False
    elif direction == 4:
      self.down = False

  def update(self, tick):
    # Movment and Animation
    self.did_animate = False # Have we animated anything this frame

    if self.left: # Left
      self.last_direction = 1
      self.did_animate = True
      for tile in self.all_tiles:
        tile.left(self.speed)
        if tick % self.animation_timer == 0:
          self.animation_itteration += 1

          if self.animation_itteration+1 > len(self.animation_left):
            self.animation_itteration = -1
          self.image = self.animation_left[self.animation_itteration]

    elif self.right: # Right
      self.last_direction = 2
      self.did_animate = True
      for tile in self.all_tiles:
        tile.right(self.speed)
        if tick % self.animation_timer == 0:
          self.animation_itteration += 1

          if self.animation_itteration+1 > len(self.animation_right):
            self.animation_itteration = -1
          self.image = self.animation_right[self.animation_itteration]

    if self.up: # Up
      self.last_direction = 3
      self.did_animate = True
      for tile in self.all_tiles:
        tile.up(self.speed)
        if tick % self.animation_timer == 0:
          self.animation_itteration += 1

          if self.animation_itteration+1 > len(self.animation_up):
            self.animation_itteration = -1
          self.image = self.animation_up[self.animation_itteration]

    elif self.down: # Down
      self.last_direction = 4
      self.did_animate = True
      for tile in self.all_tiles:
        tile.down(self.speed)
        if tick % self.animation_timer == 0:
          self.animation_itteration += 1

          if self.animation_itteration+1 > len(self.animation_down):
            self.animation_itteration = -1
          self.image = self.animation_down[self.animation_itteration]
    
    if not self.did_animate: # Standing still animation 
      self.image = self.animation_still[self.last_direction-1]

    # collision 
    for tile in self.collide_tiles:
      if self.rect.colliderect(tile):
        if tile.rect.midright[0] > self.rect.midleft[0]: # left
          self.left = False
        if tile.rect.midleft[0] < self.rect.midright[0]: # right
          self.right = False
        if self.rect.midtop[1] <= tile.rect.midbottom[1]: # up
          self.up = False
        if tile.rect.midtop[1] <= self.rect.midbottom[1]: # down
          self.down = False

  def candy_check(self):
    for candy in self.candy:
      if self.rect.colliderect(candy) and candy.type == 'b':
        candy.type = 's'
        candy.image = Images.trans
        return True
    return False
      
  def ghost_check(self, ghost):
    if self.rect.colliderect(ghost):
      return True
    else: 
      return False
