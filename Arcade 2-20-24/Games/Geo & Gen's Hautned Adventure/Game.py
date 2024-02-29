# Main Game Class  
import pygame, Images, Player, Tiles, Maps, time

class Game(pygame.sprite.Sprite):
  def __init__(self, screen, screen_width, screen_height):
    pygame.sprite.Sprite.__init__(self)
    self.sprites = pygame.sprite.Group()
    self.wall_tiles = pygame.sprite.Group()
    self.all_tiles = pygame.sprite.Group()
    self.candy = pygame.sprite.Group()
    self.player = Player.Player(self.wall_tiles, self.all_tiles, self.candy, screen_width, screen_height)
    self.map = Maps.Map1
    self.candy_gathered = int(0)
    self.candy_total = int(0)
    self.tick_count = int(0)
    self.screen = screen
    self.screen_width = screen_width
    self.screen_height = screen_height
    self.won = False
    self.font = pygame.font.Font('freesansbold.ttf', 32)
    
    for i in range(len(self.map)): # Map generation 
      for x in range(len(self.map[i])):
        self.exists = Tiles.Tile(self.map[i][x], i, x)
        self.sprites.add(self.exists)
        self.all_tiles.add(self.exists)
        if self.exists.type == 'w': # Wall
          self.wall_tiles.add(self.exists) 
        elif self.exists.type == 'b': # Candy
          self.candy_total += 1
          self.candy.add(self.exists)
        elif self.exists.type == 'c': # Ghost
          self.ghost = self.exists
      del self.exists
 
    self.sprites.add(self.player) # Adding player to sprite group

  def update(self):
    self.tick_count += 1 
    if self.player.candy_check():
      self.candy_gathered += 1
    self.screen.blit(Images.dirt, (0,0)) # Background Image
    self.sprites.draw(self.screen) # Drawing all Sprites including map
    self.player.update(self.tick_count) # Player update 
    self.screen.blit(Images.view_frame,(0,0)) # Bliting black square 

    if self.player.ghost_check(self.ghost): # Ghost Collision 
      if self.candy_total - self.candy_gathered <= 0: # Did we win and touch the ghost? 
        self.ghost.image = Images.ghost_happy
        self.ghost_text = self.font.render('Thank you', True, "orange")
        self.won = True # Stopping Game after frame is drawn
      else:
        self.ghost_text = self.font.render('I lost my candy :( please get it', True, "orange")
      self.screen.blit(self.ghost_text, (self.screen_width//2-200, self.screen_height//2-50)) # Displays ghost text while touching Ghost 

    self.candy_display = self.font.render('Candy Left: %s' % (int(self.candy_total) - int(self.candy_gathered)), True, "white") # Candy Counter 
    self.screen.blit(self.candy_display, (20,20))
    self.timer = self.font.render('%s' % (int(self.tick_count) // int(60)), True, "white")
    self.screen.blit(self.timer, (self.screen_width-80,20))

    # Screen Decerations 
    self.screen.blit(Images.happy_pumpkin, (10, 100))
    self.screen.blit(Images.sad_skelly, (self.screen_width-270, 480))

    if self.won: # Win Check
      self.end()

  def end(self):
    self.screen.blit(Images.dirt, (0,0)) # Background Image
    self.sprites.draw(self.screen) # Drawing all Sprites including map
    self.player.update(self.tick_count) # Player update 
    self.screen.blit(Images.view_frame,(0,0)) # Bliting black square
    self.ghost_text = self.font.render('Thank you', True, "orange")
    self.screen.blit(self.ghost_text, (self.screen_width//2-80, self.screen_height//2-50)) # Displays ghost text while touching Ghost 


    pygame.display.update()
    time.sleep(5)
    self.kill()
    pygame.quit()
