# Geo & Gem's Haunted Adventure 10-23-2 
# Main
import pygame, Game

pygame.init()
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 825
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Geo & Gem's Haunted Adventure")

# Game Variables 
clock = pygame.time.Clock()
FPS = 45
game = Game.Game(screen, SCREEN_WIDTH, SCREEN_HEIGHT)
while True:
  clock.tick(FPS)
  screen.fill('black') # (89, 62, 60)
  game.update()

  # Event Gatherer  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      break
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_a:
        game.player.movestart(1)
      if event.key == pygame.K_d:
        game.player.movestart(2)
      if event.key == pygame.K_w:
        game.player.movestart(3)
      if event.key == pygame.K_s:
        game.player.movestart(4)
    elif event.type == pygame.KEYUP:
      if event.key == pygame.K_a:
        game.player.movestop(1)
      if event.key == pygame.K_d:
        game.player.movestop(2)
      if event.key == pygame.K_w:
        game.player.movestop(3)
      if event.key == pygame.K_s:
        game.player.movestop(4)

  pygame.display.update()
