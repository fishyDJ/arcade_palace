# Webbs Wackey game maker 12-24-23 
import pygame, subprocess

class Thing_On_Screen(pygame.sprite.Sprite):
  def __init__(self, image, x, y):
    pygame.sprite.Sprite.__init__(self)
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.centerx = x
    self.rect.centery = y

class circles(pygame.sprite.Sprite):
  def __init__(self, images, x, y, index_number):
    pygame.sprite.Sprite.__init__(self)
    self.images = images
    self.image = self.images[0]
    self.rect = self.image.get_rect()
    self.rect.centerx = x
    self.rect.centery = y
    self.index_number = index_number

  def update(self, new_index):
    if new_index == self.index_number:
      self.image = self.images[1]
    else:
      self.image = self.images[0]


def play_da_game(directory): # Calls game applications 
  pygame.display.set_mode((1, 1))
  subprocess.run(["python", directory])
  pygame.display.set_mode((screen_width, screen_height))

pygame.init()
pygame.mixer.init()

# Set up the game window
screen_width = 1000
screen_height = 900
screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Arcade Palace")
bg_color = '#918e97'

# Images
logo_img = pygame.image.load(R'Assets\logo_self_made.png')
logo = pygame.transform.smoothscale(logo_img, (600, 600))
arrow_img = pygame.image.load(R'Assets\arrow.png')
arrow_img = pygame.transform.smoothscale(arrow_img, (150, 75))
arrow_right = pygame.transform.rotate(arrow_img, angle=90)
arrow_left = pygame.transform.rotate(arrow_img, angle=-90)

#scrolling img
connect4_showcase = pygame.image.load(R"Assets\Connect4_showcase.PNG")
geogem_showcase = pygame.image.load(R"Assets\snip_of_geogem.PNG")
geogemH_showcase = pygame.image.load(R"Assets\GeogemH_Showcase.PNG")
pong_showcase = pygame.image.load(R"Assets\POOOOONNNNGGGG.PNG")
ponder_showcase = pygame.image.load(R"Assets\ponder.PNG")
ponder_showcase = pygame.transform.smoothscale(ponder_showcase, (400, 300))
pong_showcase = pygame.transform.smoothscale(pong_showcase, (400, 300))
geogemH_showcase = pygame.transform.smoothscale(geogemH_showcase, (400, 300))
geogem_showcase = pygame.transform.smoothscale(geogem_showcase, (400, 300))
connect4_showcase = pygame.transform.smoothscale(connect4_showcase, (400, 300))

# circles
open_circle = pygame.image.load(R"Assets\open_circle.png")
filled_circle = pygame.image.load(R"Assets\filled_circle.png")
open_circle = pygame.transform.smoothscale(open_circle, (75, 75))
filled_circle = pygame.transform.smoothscale(filled_circle, (75, 75))

# Screen Sprites 
ponder_showcase = Thing_On_Screen(ponder_showcase, 505, 500)
geogemh_showcase = Thing_On_Screen(geogemH_showcase, 505, 500)
connect4_showcase = Thing_On_Screen(connect4_showcase, 505, 500)
geogem_showcase = Thing_On_Screen(geogem_showcase, 505, 500)
pong_showcase = Thing_On_Screen(pong_showcase, 505, 500)

# Screen Sprite Groups
your_guess_is_as_good_as_mine = 0
screen1 = pygame.sprite.Group()
screen1.add(connect4_showcase)
screen2 = pygame.sprite.Group()
screen2.add(geogem_showcase)
screen3 = pygame.sprite.Group()
screen3.add(geogemh_showcase)
screen4 = pygame.sprite.Group()
screen4.add(pong_showcase)
screen5 = pygame.sprite.Group()
screen5.add(ponder_showcase)

list_of_screens = [ # Tracks current screen, and its acompanying variables/music 
  (screen1,"Games\Connect 4\Connect4.py", connect4_showcase, "Assets\cartride.mp3"), 
  (screen2,"Games\Geo_Gem\Main.py", geogem_showcase, "Assets\helldivers.mp3"), 
  (screen3,"Games\Geo & Gen's Hautned Adventure\Geo_GemH.py", geogemh_showcase, "Assets\jalaofun.mp3"), 
  (screen4,"Games\Ping_Pong\pingpong.py", pong_showcase, "Assets\jugg-jingle.mp3"), 
  (screen5,"Games\Wanderandponder\wanderandponder.py", ponder_showcase, "Assets\white-night.mp3")
  ]

# Constant Sprites
displayables = pygame.sprite.Group()
displayables.add(Thing_On_Screen(logo_img, screen_width/2 + 12, 170))
left_arrow = Thing_On_Screen(arrow_right, screen_width * 8/10 -2, 488)
displayables.add(left_arrow)
right_arrow = Thing_On_Screen(arrow_left, screen_width/5 +10, 488)
displayables.add(right_arrow)

# Circles
circle_images = [open_circle, filled_circle]
circles_list = pygame.sprite.Group()
circles_list_not_sprite = []
for i in range(1,6):
  itterable = circles(circle_images, screen_width/4 - 47 + i*100, 730, i-1)
  circles_list.add(itterable)
  circles_list_not_sprite.append(itterable)

# Main loop
clock = pygame.time.Clock()
pygame.mixer.music.load(f'Assets\cartride.mp3')
pygame.mixer.music.play(-1)

while True:
  started_screen = your_guess_is_as_good_as_mine
  screen.fill(bg_color)
  displayables.draw(screen)
  circles_list.update(your_guess_is_as_good_as_mine)
  circles_list.draw(screen)
  list_of_screens[your_guess_is_as_good_as_mine][0].draw(screen)
 
  # Event handler
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
        
    if event.type == pygame.MOUSEBUTTONDOWN: # Click Detection
      pos = pygame.mouse.get_pos()
      if left_arrow.rect.collidepoint(pos): # Left Arrow 
        if your_guess_is_as_good_as_mine <= 3:
          your_guess_is_as_good_as_mine += 1
      elif right_arrow.rect.collidepoint(pos): # Right Arrow
        if your_guess_is_as_good_as_mine >= 1:
          your_guess_is_as_good_as_mine -= 1
      elif list_of_screens[your_guess_is_as_good_as_mine][2].rect.collidepoint(pos): # Game Play 
        play_da_game(list_of_screens[your_guess_is_as_good_as_mine][1])
      else: # Circles
        iteration = -1
        for circle in circles_list_not_sprite:
          iteration +=1
          if circle.rect.collidepoint(pos):
            your_guess_is_as_good_as_mine = iteration 

  if started_screen != your_guess_is_as_good_as_mine:
    pygame.mixer.music.load(list_of_screens[your_guess_is_as_good_as_mine][3])
    pygame.mixer.music.play(-1)

  clock.tick(60)
  pygame.display.update()
