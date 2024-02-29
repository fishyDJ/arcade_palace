# group project 2/23/2023
# Primary Coder - Austin, Graphic Designer - Destiny, Recorder - Luke, Researcher/Manager - McKayla
import pygame

class tile(pygame.sprite.Sprite):
  def __init__(self, tile_type, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.tile_type = tile_type
    self.x = (x * 75)-75
    self.y = (y * 75)-75
    if self.tile_type == 'p':
      self.y += 5
    if self.tile_type == 'b':
      self.image = pygame.image.load(R'Games\Geo_Gem\assets\groundtile.png').convert_alpha()
    elif self.tile_type == 'p':
      self.image = pygame.image.load(R'Games\Geo_Gem\assets\spiketile.png').convert_alpha()
    elif self.tile_type == 'l':
      self.image = pygame.image.load(R'Games\Geo_Gem\assets\lavatile.png').convert_alpha()
    else:
      self.image = pygame.image.load(R'Games\Geo_Gem\assets\transparenttile.png').convert_alpha()
    if self.tile_type == 's':
      self.kill()
    self.rect = self.image.get_rect()
    self.rect.x = self.x
    self.rect.y = self.y


class Player(pygame.sprite.Sprite):  # there will always be 2 of these
  def __init__(self, number, starting_x, starting_y, grid):
    pygame.sprite.Sprite.__init__(self)
    self.number = number
    self.images = []
    for i in range(1,4):
      img = pygame.image.load(F'Games\Geo_Gem\Assets\player{self.number}_img{i}.png')
      self.images.append(img)
    self.image = self.images[1]
    self.rect = self.image.get_rect()
    self.rect.centerx = starting_x
    self.rect.centery = starting_y
    self.jumping = False # 2x2
    self.jumping_time = 0
    self.moving_right = False
    self.moving_left = False
    self.touching_ground = False
    self.falling = False
    self.grid = grid
    self.tile_pos = (1,1)
    self.hasjumped = False
    self.animation_timing = 0 
    self.animation_progress = 0
    self.direction = True # True = right
    self.hasgem = False
    self.dead = False
 
  def update(self):
    global tiles, objects, door
    # object collision
    for object in objects:
      if pygame.sprite.collide_rect(self, object):
        if type(object) == Door:
          door = object
          if not object.shut:
            if object.rect.x <= self.rect.x:
              self.moving_left = False
            if object.rect.x >= self.rect.x:
              self.moving_right = False
        if type(object) == Gem:
          if object.number == self.number:
            object.kill()
            self.hasgem = True
        if type(object) == Exitt:
          exitable = True
          for player in players:
            if not player.hasgem:
              exitable = False
          if exitable:
            self.dead = True
            self.kill()

    #  verticle
    self.falling = False
    x = self.rect.centerx
    y = self.rect.centery
    xt = x // 75
    yt = y // 75
    self.tile_pos = (xt + 1, yt + 1)
    tilebelow = self.tile_pos[1] * 16 + self.tile_pos[0] - 1
    tileabove = self.tile_pos[1] * 16 + self.tile_pos[0] - 33
    tileright = self.tile_pos[1] * 16 + self.tile_pos[0] - 16
    tileleft = self.tile_pos[1] * 16 + self.tile_pos[0] - 18
    tileon = self.tile_pos[1] * 16 + self.tile_pos[0] - 17
    if self.jumping: # jumping
      self.jumping_time += 1
      self.rect.y -= 5
      if self.jumping_time % 35 == 0: # jump duration
        self.jumping = False
        self.jumping_time = 0
      if self.grid[tileabove] == 'b' or self.grid[tileabove] == 'l': # sky detection  
        bellow_ground = self.tile_pos[1] * 75 - 30
        distance_above = (y - bellow_ground)
        if distance_above <= -7:
          self.jumping = False
          self.jumping_time = 0

    if self.grid[tilebelow] == 'b': # ground collision bellow player
      self.touching_ground = True
    elif self.grid[tilebelow] != 'b':
      self.touching_ground = False
    if self.grid[tilebelow] == 'p':
      above_ground = self.tile_pos[1] * 75 - 30
      if self.rect.centery > above_ground:
        gameover()
    if self.grid[tilebelow] == 'l':
      above_ground = self.tile_pos[1] * 75 - 30
      if self.rect.centery > above_ground:
        #pygame.mixer.music.load(f'assets\lava splash.mp3')
        #pygame.mixer.music.play()
        gameover()
    if self.grid[tileon] == 'p':
      gameover()

    if self.touching_ground is False and not self.jumping: # falling
      self.rect.y += 5
      self.falling = True

    if self.touching_ground and not self.jumping: # slow fall
      above_ground = self.tile_pos[1] * 75 - 30
      if self.rect.centery < above_ground:
        self.rect.y += 5
        self.falling = True

    # horizontal
    distance_left =  self.rect.x - self.tile_pos[0] * 75 + 88
    distance_right = self.tile_pos[0] * 75 - self.rect.x - 60

    if self.moving_right:
      if self.grid[tileright] != 'b' or self.grid[tileright] == None:
        self.rect.x += 5
      elif distance_right >= 5:
        self.rect.x += 5

    if self.moving_left:
      if self.grid[tileleft] != 'b' or self.grid[tileleft] == None:
        self.rect.x -= 5
      elif distance_left >= 10:
        self.rect.x -= 5

    # animation
    if self.moving_right:
      self.direction = True
     
    if self.moving_left:
      self.direction = False

    if self.moving_left or self.moving_right:
      self.animation_timing += 1
    else:
      self.animation_timing = 0

    if self.moving_right and self.animation_timing % 4 == 0: # right animation
      self.animation_progress += 1
      if self.animation_progress == 3:
        self.animation_progress = 0
      self.image = self.images[self.animation_progress]
     
    if self.moving_left and self.animation_timing % 4 == 0: # left animation
      self.animation_progress += 1
      if self.animation_progress == 3:
        self.animation_progress = 0
      self.image = pygame.transform.flip(self.images[self.animation_progress], True, False)

    if not self.jumping and not self.falling and not self.moving_left and not self.moving_right and self.direction: # stationary image
      self.image = self.images[1]
      self.hasjumped = False
    elif not self.jumping and not self.falling and not self.moving_left and not self.moving_right and not self.direction:
      self.image = pygame.transform.flip(self.images[1], True, False)
      self.hasjumped = False

    if (self.jumping or self.falling) and not self.direction: # jumping / falling
      self.image = pygame.transform.flip(self.images[2], True, False)

    if (self.jumping or self.falling) and self.direction:
      self.image = self.images[2]


class Door(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(R'Games\Geo_Gem\assets\door1.png')
    self.images = []
    for i in range(1,5):
      self.images.append(pygame.image.load(F'Games\Geo_Gem\\assets\door{i}.png'))
    self.rect = self.image.get_rect()
    self.rect.x = (x * 75) - 75
    self.rect.y = (y * 75) - 75
    self.shut = False
    self.animation_timing = 0
    self.animation_progress = 0

  def openn(self):
    self.shut = True
    self.animation_timing += 1
    if self.animation_timing %4 == 0 and self.animation_progress != 4:
      self.image = self.images[self.animation_progress]
      self.animation_progress += 1
 
  def close(self):
    self.shut = False
    self.animation_timing += 1
    if self.animation_timing %4 == 0 and self.animation_progress > 0:
      self.animation_progress -= 1
      self.image = self.images[self.animation_progress]


class Gem(pygame.sprite.Sprite):
  def __init__(self, number, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.number = number # grey = 1
    if number == 1:
      self.image = pygame.image.load(R'Games\Geo_Gem\assets\gem1.png')
    elif number == 2:
      self.image = pygame.image.load(R'Games\Geo_Gem\assets\gem2.png')
    self.rect = self.image.get_rect()
    self.rect.x = (x * 75) - 75
    self.rect.y = (y * 75) - 75


class Button(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(R'Games\Geo_Gem\assets\playerbutton.png')
    self.rect = self.image.get_rect()
    self.rect.x = (x * 75) - 75
    self.rect.y = (y * 75) - 75
    self.pressed = False

  def update(self):
    global door, players
    loop = False
    for player in players:
      if pygame.sprite.collide_rect(self, player):
        self.pressed = True
        loop = True
    if not loop:
      self.pressed = False
    if self.pressed:
      door.openn()
    else:
      door.close()


class Exitt(pygame.sprite.Sprite):
  def __init__(self, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.image.load(R'Games\Geo_Gem\assets\exit.png')
    self.rect = self.image.get_rect()
    self.rect.x = (x * 75) - 75
    self.rect.y = (y * 75) - 75

def generate(map): # map generating
  global tiles, objects, door
  screen.fill('white')
  loopx = 0
  loopy = 1
  for i in range(len(map)):
    loopx += 1
    tiles.add(tile(str(map[i]), loopx, loopy))
    if map[i] == 'd':
      door = Door(loopx, loopy)
      objects.add(door)
    if map[i] == 'e':
      objects.add(Exitt(loopx, loopy))
    if map[i] == 't':
      objects.add(Button(loopx, loopy))
    if map[i] == 'r':
      objects.add(Gem(1, loopx, loopy))
    if map[i] == 'g':
      objects.add(Gem(2, loopx, loopy))
    if loopx == 16:
      loopx = 0
      loopy += 1

def gameover():
  global playing
  geo.kill()
  gem.kill()
  playing = False
 
def next():
  global tiles, players, objects, geo, gem, objects, WINS
  for sprite in tiles:
    sprite.kill()
  for player in players:
    player.kill()
  for object in objects:
    object.kill()
  geo = Player(1, 110, SCREEN_HEIGHT - 110, MAP1)
  gem = Player(2, 180, SCREEN_HEIGHT - 110, MAP1)
  players.add(geo, gem)
  generate(MAP1)
  pygame.time.wait(300)
  #pygame.mixer.music.load(f'assets\cave music.mp3')
  #pygame.mixer.music.play()
  if WINS == 1:
    gameover()
  WINS += 1


if __name__ == '__main__': # Start Point
  pygame.init()
  #pygame.mixer.init()
  SCREEN_WIDTH = 1200
  SCREEN_HEIGHT = 825
  FPS = 45 # 40
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  pygame.display.set_caption("Geo_Gem")
  BACKGROUNGIMAGE = pygame.image.load(R'Games\Geo_Gem\assets\cave bg.png')

  tiles = pygame.sprite.Group()
  players = pygame.sprite.Group()
  objects = pygame.sprite.Group()
  clock = pygame.time.Clock()
        
  # s = Sky, l = Lava, p = Spikes, b = Ground, e = exit, d = door, t = button, r = gem1, g = gem2  11x16
  SMAP = [
  's','s','s','s','s','s','s','s','s','s','s','s','s','s','s','s',
  's','s','s','s','s','s','s','s','s','s','s','s','s','s','s','s',
  's','s','s','s','s','s','s','s','s','s','s','s','s','s','s','s',
  's','s','s','s','s','s','s','s','s','s','s','s','s','s','s','s',
  's','s','s','s','s','s','s','s','s','s','s','s','s','s','s','s',
  's','s','s','s','s','s','s','s','s','s','s','s','s','s','s','s',
  's','s','s','s','s','s','s','s','s','s','s','s','s','s','s','s',
  's','s','s','s','s','s','s','s','s','s','s','s','s','s','s','s',
  's','s','s','s','s','s','s','s','s','s','s','s','s','s','s','s',
  'p','p','s','s','s','p','p','s','s','s','s','s','p','p','p','p',
  'b','b','l','l','l','b','b','b','b','l','l','l','b','b','b','b',
  ]

  MAP1 = [
  'b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b',
  'b','s','s','s','s','e','s','s','s','s','s','s','s','s','s','b',
  'b','s','s','s','s','b','b','b','b','b','s','s','s','s','s','b',
  'b','r','s','s','s','s','s','s','s','s','s','s','b','l','l','b',
  'b','b','l','b','s','s','s','s','s','s','s','s','s','s','s','b',
  'b','s','s','b','s','s','s','s','b','b','b','s','s','s','s','b',
  'b','g','s','d','s','s','s','s','s','s','s','s','s','p','p','b',
  'b','b','b','b','b','s','s','s','s','s','s','b','b','b','b','b',
  'b','s','s','s','s','s','s','b','b','b','s','s','s','s','s','b',
  'b','s','s','s','s','s','s','s','s','s','s','s','s','s','t','b',
  'b','b','b','b','b','b','b','l','l','l','b','b','b','b','b','b',
  ]
  # s = Sky, l = Lava, p = Spikes, b = Ground, e = exit, d = door, t = button, r = gem1, g = gem2  11x16
  MAP2 = [
  'b','b','b','b','b','b','b','b','b','b','b','b','b','b','b','b',
  'b','s','s','s','s','s','s','s','s','s','s','s','s','e','s','b',
  'b','s','s','s','s','b','b','b','b','s','s','s','b','b','b','b',
  'b','g','s','s','s','s','s','s','s','s','s','s','s','p','p','b',
  'b','b','l','l','b','s','s','p','s','s','s','b','b','b','b','b',
  'b','s','s','s','s','s','s','b','b','s','s','b','s','s','s','b',
  'b','p','p','s','s','s','s','s','s','s','s','d','s','r','s','b',
  'b','b','b','b','s','s','s','s','s','s','b','b','b','b','b','b',
  'b','s','s','s','s','s','s','b','b','s','s','s','s','s','s','b',
  'b','s','s','s','s','s','s','s','s','s','s','s','s','t','p','b',
  'b','b','b','b','l','l','b','b','b','b','l','b','b','b','b','b',
  ]

  #pygame.mixer.music.load(f'assets\cave music.mp3')
  WINS = 0
  timer = 0
  timeimg = pygame.image.load(R'Games\Geo_Gem\Assets\thing.png')
  font = pygame.font.Font('freesansbold.ttf', 32)


  # splash screen
  splashing = True
  generate(SMAP)
  splashimage = pygame.image.load(R'Games\Geo_Gem\assets\start.png')

  while splashing:
    clock.tick(FPS)
    screen.blit(BACKGROUNGIMAGE, (0, 0))
    tiles.draw(screen)
    screen.blit(splashimage, (SCREEN_WIDTH/2 - 210, SCREEN_WIDTH/2 - 210))
    splashrect = splashimage.get_rect()
    splashrect.x = SCREEN_WIDTH/2 - 210
    splashrect.y = SCREEN_WIDTH/2 - 210
    font = pygame.font.Font('freesansbold.ttf', 32)
    sstext = font.render('Join Geo and Gem on their adventure! Use WASD to move Geo (gray)', True, "white")
    sstext2 = font.render(' and the arrow keys to move Gem (blue). Collect the gem crystals', True, 'white')
    sstext3 = font.render('While avoiding the lava and spikes to escape the cave and get the treasure!', True, 'white')
    screen.blit(sstext, (50, 200))
    screen.blit(sstext2, (80, 250))
    screen.blit(sstext3, (0,300))
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        playing = False
        splashing = False
      if event.type == pygame.MOUSEBUTTONUP:
        pos = pygame.mouse.get_pos()
        if splashrect.collidepoint(pos):
          splashing = False
    pygame.display.update()

  exitscreen = True
  while exitscreen:
    door = None
    # game variables
    for sprite in tiles:
      sprite.kill()
    geo = Player(1, 110, SCREEN_HEIGHT - 110, MAP2)
    gem = Player(2, 180, SCREEN_HEIGHT - 110, MAP2)
    players.add(geo, gem)
    generate(MAP2)
    playing = True
    t = 0
    #pygame.mixer.music.load(f'assets\cave music.mp3')
    #pygame.mixer.music.play()
    music_timer = 0


    # game loop
    while playing:
      clock.tick(FPS)
      music_timer += 1
      timer += 1
      if music_timer // FPS == 64:
        #pygame.mixer.music.play()
        music_timer = 0
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          playing = False
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_w and not geo.hasjumped:
            geo.jumping = True
            geo.hasjumped = True
          if event.key == pygame.K_a:
            geo.moving_left = True
          if event.key == pygame.K_d:
            geo.moving_right = True

          if event.key == pygame.K_UP and not gem.hasjumped:
            gem.jumping = True
            gem.hasjumped = True
          if event.key == pygame.K_LEFT:
            gem.moving_left = True
          if event.key == pygame.K_RIGHT:
            gem.moving_right = True

        if event.type == pygame.KEYUP:
          if event.key == pygame.K_a:
            geo.moving_left = False
          if event.key == pygame.K_d:
            geo.moving_right = False
          if event.key == pygame.K_LEFT:
            gem.moving_left = False
          if event.key == pygame.K_RIGHT:
            gem.moving_right = False
      t = 0
      for player in players:
        t += 1
      if t == 0:
        next()
      players.update()
      objects.update()
      screen.fill('white')
      screen.blit(BACKGROUNGIMAGE, (0, 0))
      tiles.draw(screen)
      objects.draw(screen)
      players.draw(screen)
      screen.blit(timeimg, (SCREEN_WIDTH / 2 - 90, 0))
      time_display1 = timer//FPS
      time_display2 = time_display1 // 60
      time_display3 = time_display1 - time_display2 * 60
      if time_display3 <= 9:
        displayed_time =  str(time_display2) + ': 0' + str(time_display3)
      else:
        displayed_time = str(time_display2) + ':' + str(time_display3)
      timertext = font.render(displayed_time, True, "white")
      screen.blit(timertext, (SCREEN_WIDTH / 2 - 40, 20))
      pygame.display.update()

    for tille in tiles:
      tille.kill()
    for player in players:
      player.kill()
    for object in objects:
      object.kill()
    generate(SMAP)
    splashimage = pygame.image.load(R'Games\Geo_Gem\assets\start.png')
    splashimage2 = pygame.image.load(R'Games\Geo_Gem\assets\stop button.png')
    closingsplash = True

    while closingsplash:
      clock.tick(FPS)
      screen.blit(BACKGROUNGIMAGE, (0, 0))
      tiles.draw(screen)
      screen.blit(splashimage, (SCREEN_WIDTH/2 - 410, SCREEN_WIDTH/2 - 210))
      screen.blit(splashimage2, (SCREEN_WIDTH/2, SCREEN_WIDTH/2 - 205))
      splashrect = splashimage.get_rect()
      splashrect.x = SCREEN_WIDTH/2 - 410
      splashrect.y = SCREEN_WIDTH/2 - 205
      splashrect2 = splashimage.get_rect()
      splashrect2.x = SCREEN_WIDTH/2
      splashrect2.y = SCREEN_WIDTH/2 - 210
      sstext = font.render('Press Start to play agin', True, "white")
      sstext2 = font.render('Press Stop to exit', True, 'white')
      sstext3 = font.render('Your time was: ' + displayed_time, True, 'white')
      screen.blit(sstext, (400, 200))
      screen.blit(sstext2, (440, 250))
      screen.blit(sstext3, (420, 300))

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          closingsplash = False
          exitscreen = False
        if event.type == pygame.MOUSEBUTTONUP:
          pos = pygame.mouse.get_pos()
          if splashrect.collidepoint(pos):
            closingsplash = False
            exitscreen = True
            WINS = 0
            #tim
          if splashrect2.collidepoint(pos):
            closingsplash = False
            exitscreen = False
      pygame.display.update()
  pygame.quit()
