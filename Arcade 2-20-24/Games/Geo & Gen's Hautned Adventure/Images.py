# Images
import pygame

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 825
# Player Size: 80x80
# Tile Size: 120x120

wall = pygame.image.load(R"Games\Geo & Gen's Hautned Adventure\Assets\corn.jpg")
wall = pygame.transform.smoothscale(wall, (120, 120))
dirt = pygame.image.load(R"Games\Geo & Gen's Hautned Adventure\Assets\dirt.jpg")
dirt = pygame.transform.smoothscale(dirt, (SCREEN_WIDTH, SCREEN_HEIGHT))
trans = pygame.image.load(R"Games\Geo & Gen's Hautned Adventure\Assets\transparenttile.png")
trans = pygame.transform.smoothscale(trans, (120, 120))
player_still = pygame.image.load(R"Games\Geo & Gen's Hautned Adventure\Assets\player_still.png")
player_still_right = pygame.transform.smoothscale(player_still, (80, 80)) # Player Size
player_still_left = pygame.transform.flip(player_still_right, True, False)
player_still_up = pygame.transform.rotate(player_still_right, 90)
player_still_down = pygame.transform.rotate(player_still_right, 270)
player_right1 = pygame.image.load(R"Games\Geo & Gen's Hautned Adventure\Assets\player_moving1.png")
player_right1 = pygame.transform.smoothscale(player_right1, (80, 80))
player_right2 = pygame.image.load(R"Games\Geo & Gen's Hautned Adventure\Assets\player_moving2.png")
player_right2 = pygame.transform.smoothscale(player_right2, (80, 80))
player_left1 = pygame.transform.flip(player_right1, True, False)
player_left2 = pygame.transform.flip(player_right2, True, False)
player_up1 = pygame.transform.rotate(player_right1, 90)
player_up2 = pygame.transform.rotate(player_right2, 90)
player_down1 = pygame.transform.rotate(player_right1, 270)
player_down2 = pygame.transform.rotate(player_right2, 270)
view_frame = pygame.image.load(R"Games\Geo & Gen's Hautned Adventure\Assets\Frame.png")
candy_green = pygame.image.load(R"Games\Geo & Gen's Hautned Adventure\Assets\green candy.PNG")
candy_orange = pygame.image.load(R"Games\Geo & Gen's Hautned Adventure\Assets\orange candy.PNG")
candy_green = pygame.transform.smoothscale(candy_green, (120, 120))
candy_orange = pygame.transform.smoothscale(candy_orange, (120, 120))
ghost = pygame.image.load(R"Games\Geo & Gen's Hautned Adventure\Assets\sad ghost.PNG")
ghost = pygame.transform.smoothscale(ghost, (100, 100)) # Ghost
ghost_happy = pygame.image.load(R"Games\Geo & Gen's Hautned Adventure\Assets\happy ghost.PNG")
ghost_happy = pygame.transform.smoothscale(ghost_happy, (100, 100))

# Decorative Assets
sad_pumpkin = pygame.image.load(R"Games\Geo & Gen's Hautned Adventure\Assets\sad pumpkin.PNG")
happy_pumpkin = pygame.image.load(R"Games\Geo & Gen's Hautned Adventure\Assets\happy pumpkin.PNG")
sad_skelly = pygame.image.load(R"Games\Geo & Gen's Hautned Adventure\Assets\sad skelly.PNG")

sad_pumpkin = pygame.transform.smoothscale(sad_pumpkin, (200, 200))
happy_pumpkin = pygame.transform.smoothscale(happy_pumpkin, (250, 250))
sad_skelly = pygame.transform.smoothscale(sad_skelly, (250, 250))
