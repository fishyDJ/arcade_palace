import pygame
import sys
import random
import time

# Define states
MAIN_MENU = 0
GAME_SCREEN = 1
SETTINGS_SCREEN = 2

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()
screen_width = int(1280 * 0.6)
screen_height = int(960 * 0.6)
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pong")

# Colors
bg_color = (235, 235, 235)
dark_green = (1, 50, 32)
light_grey = (200, 200, 200)

# Game objects
ball = pygame.Rect(screen_width // 2 - 9, screen_height // 2 - 9, 18, 18)
ball2 = pygame.Rect(screen_width // 2 - 9, screen_height // 2 - 9, 18, 18)
player = pygame.Rect(screen_width - 12, screen_height // 2 - 56, 6, 112)
opponent = pygame.Rect(6, screen_height // 2 - 56, 6, 112)
ball_speed_x = int(7 * random.choice((1, -1)) * 0.6)
ball_speed_y = int(7 * random.choice((1, -1)) * 0.6)
ball2_speed_x = int(3 * random.choice((1, -1)) * 0.6)
ball2_speed_y = int(3 * random.choice((1, -1)) * 0.6)
player_speed = 0
player2_speed = 0
opponent_speed = int(5)
p2 = 0  # 2 playe
ball_2 = False

#image
image = pygame.image.load("ping_pong_game/assets/RULES.png")  # Replace with the actual image path
image_rect = image.get_rect()
image_rect.center = (screen_width // 2, screen_height // 2)
message = True


# Text variables
player_score = 0
opponent_score = 0
game_font = pygame.font.Font(None, 32)
score_time = True

   
def ball_animation():
    global ball_speed_x, ball_speed_y, opponent_score, player_score, score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1
    if ball.left <= 0:
        player_score += 1
        score_time = pygame.time.get_ticks()
    if ball.right >= screen_width:
        opponent_score += 1
        score_time = pygame.time.get_ticks()
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1
        ball_speed_y +=  0.5
        ball_speed_x +=  0.5
def ball2_animation():
    global ball2_speed_x, ball2_speed_y, opponent_score, player_score, score_time, player
    ball2.x += ball2_speed_x
    ball2.y += ball2_speed_y
    if ball2.top <= 0 or ball2.bottom >= screen_height:
        ball2_speed_y *= -1
    if ball2.left <= 0:
        player_score += 1
        score_time = pygame.time.get_ticks()
    if ball2.right >= screen_width:
        opponent_score += 1
        score_time = pygame.time.get_ticks()
    if ball2.colliderect(player) or ball2.colliderect(opponent):
        ball2_speed_x *= -1
        ball2_speed_y += 1
        ball2_speed_x += 1
        time.sleep(0.3)
def player_animation():
    global player, player_speed
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height
def player2_animation():
    global p2
    if p2 == 1:
        opponent.y += player2_speed
        if opponent.top <= 0:
            opponent.top = 0
        if opponent.bottom >= screen_height:
            opponent.bottom = screen_height
def opponent_ai():
    global p2
    if p2 == 0:
        if ball2.x < ball.x:
            if opponent.top-10 < ball2.y:
                opponent.top += opponent_speed
            if opponent.bottom-10 > ball2.y:
                opponent.bottom -= opponent_speed
        if ball2.x > ball.x:
            if opponent.top-10 < ball.y:
                opponent.top += opponent_speed
            if opponent.bottom-10 > ball.y:
                opponent.bottom -= opponent_speed
        if opponent.top <= 0:
            opponent.top = 0
        if opponent.bottom >= screen_height:
            opponent.bottom = screen_height
def ball_restart():
    global ball_speed_x, ball_speed_y, score_time, ball2_speed_x, ball2_speed_y
    current_time = pygame.time.get_ticks()
    ball.center = (screen_width / 2, screen_height / 2)
    ball2.center = (screen_width / 2, screen_height / 2)
    if current_time - score_time < 700:
        number_three = game_font.render("3", False, light_grey)
        screen.blit(number_three, (screen_width / 2 - 10, screen_height / 2 + 20))
    if 700 < current_time - score_time < 1400:
        number_number = game_font.render("2", False, light_grey)
        screen.blit(number_number, (screen_width / 2 - 10, screen_height / 2 + 20))
    if 1400 < current_time - score_time < 2100:
        number_one = game_font.render("1", False, light_grey)
        screen.blit(number_one, (screen_width / 2 - 10, screen_height / 2 + 20))
    if current_time - score_time < 2100:
        ball_speed_x, ball_speed_y = 0, 0
        ball2_speed_x, ball2_speed_y = 0, 0
    else:
        ball_speed_y = 4 * random.choice((1, -1))
        ball_speed_x = 4 * random.choice((1, -1))
        ball2_speed_y = 2 * random.choice((1, -1))
        ball2_speed_x = 2 * random.choice((1, -1))
        if ball_speed_x - 2 == ball2_speed_x:
            ball2_speed_x = 2 * (-1)
        score_time = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                message = False
            if event.key == pygame.K_DOWN:
                player_speed += int(8)
            if event.key == pygame.K_UP:
                player_speed -= int(8)
            if p2 == 1:  # player 2
                if event.key == pygame.K_w:
                    player2_speed -= int(7)
                if event.key == pygame.K_s:
                    player2_speed += int(7)
            if event.key == pygame.K_2:
                p2 = 1
            if event.key == pygame.K_3:
                p2 = 0
            if event.key == pygame.K_1:
                ball_2 = True  # Start the second ball
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= int(8)
            if event.key == pygame.K_UP:
                player_speed += int(8)
            if p2 == 1:  # player 2
                if event.key == pygame.K_w:
                    player2_speed += int(7)
                if event.key == pygame.K_s:
                    player2_speed -= int(7)

    if not message:
        ball_animation()

    if ball_2:
        ball2_animation()
    player_animation()
    opponent_ai()
    player2_animation()

    # Visuals
    screen.fill(bg_color)
    # Blit the image onto the screen
    if message:
        screen.blit(image, image_rect)
    pygame.draw.rect(screen, dark_green, player)
    pygame.draw.rect(screen, dark_green, opponent)
    if not message:
        pygame.draw.ellipse(screen, dark_green, ball)
    
    if ball_2:
        pygame.draw.ellipse(screen, dark_green, ball2)
    
    pygame.draw.aaline(screen, dark_green, (screen_width // 2, 0), (screen_width // 2, screen_height))




    if score_time:
        ball_restart()
    player_text = game_font.render(f"{player_score}", True, light_grey)
    opponent_text = game_font.render(f"{opponent_score}", True, light_grey)
    if not message:
        screen.blit(player_text, (int(660 * 0.6), int(470 * 0.6)))
        screen.blit(opponent_text, (int(600 * 0.6), int(470 * 0.6)))

    pygame.display.flip()
    clock.tick(60)