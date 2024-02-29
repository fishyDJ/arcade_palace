import pygame
import sys

#  MAKE dots where points are, TIME BASED/score




# Initialize Pygame
pygame.init()
bg_img = pygame.image.load(R"Games\Wanderandponder\Assets\mapforwanderandponder.png")
cat = pygame.image.load(R"Games\Wanderandponder\Assets\blackcat.png")
burp = pygame.image.load(R"Games\Wanderandponder\Assets\glowpurpleball.png")
purp = pygame.transform.scale(burp, (25, 25))
image_rect = bg_img.get_rect()
screen_height = image_rect.height
screen_width = image_rect.width
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Wander and Ponder")

#rulesbar
sx = int(screen_width/3)
sy = int(screen_height/3)
surface = pygame.Surface((sx, sy))
surface.fill("#a85124")
rules = True
font = pygame.font.Font("freesansbold.ttf", 24)
font1 = pygame.font.Font("freesansbold.ttf", 18)
font2 = pygame.font.Font("freesansbold.ttf", 70)
title = font.render("Wander and Ponder", True, ("#85bdda"))
text = font1.render("Wander with your keyboard and the cat will exsplore", True, ("#cbd2c8"))
text1 = font1.render("Find all Ponder points to achieve greatness", True, ("#cbd2c8"))
# win screen
text3 = font2.render("Omniscience Acheived", True, ("#a85124"))
surface2 = pygame.Surface((screen_width, screen_width))
surface2.fill("#247ba8")

# cat pos
x=-400
y=-400
# ponder points
pp = 0
p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13, p14 = [True] * 14
while True:
    points = font1.render(f"Ponder : {pp}/12", True, ("#cbd2c8"))
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            # Get the key pressed
            key = pygame.key.name(event.key)
            rules = False

            #column 1 
            if key == "1":
                x = screen_width* 1/10 -80 
                y = screen_height* 1/4 -130
            if key == "q":
                x = screen_width * 1/10 -80 
                y = screen_height * 2/4 -130
                if p12:
                    pp += 1
                p12 = False
            if key == "a":
                x = screen_width * 1/10 -80 
                y = screen_height * 3/4 -130
            if key == "z":
                x = screen_width * 1/10 -80 
                y = screen_height * 4/4 -190
            
            #column 2
            if key == "2":
                x = screen_width * 2/10 -80 
                y = screen_height/4 -130
            if key == "w":
                x = screen_width * 2/10 -80 
                y = screen_height * 2/4 -130
                if p5:
                    pp += 1
                p5 = False
            if key == "s":
                x = screen_width * 2/10 -80 
                y = screen_height * 3/4 -130
            if key == "x":
                x = screen_width * 2/10 -80 
                y = screen_height * 4/4 -190
                
            #column 3
            if key == "3":
                x = screen_width * 3/10 -80 
                y = screen_height/4 -130
            if key == "e":
                x = screen_width * 3/10 -80 
                y = screen_height * 2/4 -130
            if key == "d":
                x = screen_width * 3/10 -80 
                y = screen_height * 3/4 -130
            if key == "c":
                x = screen_width * 3/10 -80 
                y = screen_height * 4/4 -190
                
            #column 4
            if key == "4":
                x = screen_width * 4/10 -80 
                y = screen_height/4 -130
                if p1:
                    pp += 1
                p1 = False
            if key == "r":
                x = screen_width * 4/10 -80 
                y = screen_height * 2/4 -130
            if key == "f":
                x = screen_width * 4/10 -80 
                y = screen_height * 3/4 -130
                if p6:
                    pp += 1
                p6 = False
            if key == "v":
                x = screen_width * 4/10 -80 
                y = screen_height * 4/4 -190
            
            #column 5
            if key == "5":
                x = screen_width * 5/10 -80 
                y = screen_height/4 -130
                if p2:
                    pp += 1
                p2 = False
            if key == "t":
                x = screen_width * 5/10 -80 
                y = screen_height * 2/4 -130
                if p13:
                    pp += 1
                p13 = False
            if key == "g":
                x = screen_width * 5/10 -80 
                y = screen_height * 3/4 -130
            if key == "b":
                x = screen_width * 5/10 -80 
                y = screen_height * 4/4 -190
                
            #column 6
            if key == "6":
                x = screen_width * 6/10 -80 
                y = screen_height/4 -130
            if key == "y":
                x = screen_width * 6/10 -80 
                y = screen_height * 2/4 -130
            if key == "h":
                x = screen_width * 6/10 -80 
                y = screen_height * 3/4 -130
            if key == "n":
                x = screen_width * 6/10 -80 
                y = screen_height * 4/4 -190
                
            #column 7
            if key == "7":
                x = screen_width * 7/10 -80 
                y = screen_height/4 -130
            if key == "u":
                x = screen_width * 7/10 -80 
                y = screen_height * 2/4 -130
                if p11:
                    pp += 1
                p11 = False
            if key == "j":
                x = screen_width * 7/10 -80 
                y = screen_height * 3/4 -130
                if p8:
                    pp += 1
                p8 = False
            if key == "m":
                x = screen_width * 7/10 -80 
                y = screen_height * 4/4 -190
                if p7:
                    pp += 1
                p7 = False
            
            #column 8
            if key == "8":
                x = screen_width * 8/10 -80 
                y = screen_height/4 -130
                if p3:
                    pp += 1
                p3 = False
            if key == "i":
                x = screen_width * 8/10 -80 
                y = screen_height * 2/4 -130
            if key == "k":
                x = screen_width * 8/10 -80 
                y = screen_height * 3/4 -130
            if key == ",":
                x = screen_width * 8/10 -80 
                y = screen_height * 4/4 -190
                
            #column 9
            if key == "9":
                x = screen_width * 9/10 -80 
                y = screen_height/4 -130
            if key == "o":
                x = screen_width * 9/10 -80 
                y = screen_height * 2/4 -130
            if key == "l":
                x = screen_width * 9/10 -80 
                y = screen_height * 3/4 -130
                if p9:
                    pp += 1
                p9 = False
            if key == ".":
                x = screen_width * 9/10 -80 
                y = screen_height * 4/4 -190
                if p10:
                    pp += 1
                p10 = False
                
            #column 0
            if key == "0":
                x = screen_width * 10/10 -80 
                y = screen_height/4 -130
            if key == "p":
                x = screen_width * 10/10 -80 
                y = screen_height * 2/4 -130
                if p4:
                    pp += 1
                p4 = False
            if key == ";":
                x = screen_width * 10/10 -80 
                y = screen_height * 3/4 -130
            if key == "/":
                x = screen_width * 10/10 -80 
                y = screen_height * 4/4 -190

    # Update game state

    screen.blit(bg_img, (0,0))
    screen.blit(cat, (x,y))
    screen.blit(points, (30,30))
    #pupleballs
    if p1:
        screen.blit(purp, (screen_width * 4/10 -50, screen_height/4 -100))
    if p2:
        screen.blit(purp, (screen_width * 5/10 -50, screen_height/4 -100))
    if p3:
        screen.blit(purp, (screen_width * 8/10 -50, screen_height/4 -100))
    if p4:
        screen.blit(purp, (screen_width * 10/10 -50, screen_height * 2/4 -100))
    if p5:
        screen.blit(purp, (screen_width * 2/10 -50, screen_height * 2/4 -100))
    if p6:
        screen.blit(purp, (screen_width * 4/10 -50, screen_height * 3/4 -100))
    if p7:
        screen.blit(purp, (screen_width * 7/10 -50, screen_height * 4/4 -160))
    if p8:
        screen.blit(purp, (screen_width * 7/10 -50, screen_height * 3/4 -100))
    if p9:
        screen.blit(purp, (screen_width * 9/10 -50, screen_height * 3/4 -100))
    if p10:
        screen.blit(purp, (screen_width * 9/10 -50, screen_height * 4/4 -160))
    if p11:
        screen.blit(purp, (screen_width * 7/10 -50, screen_height * 2/4 -100))
    if p12:
        screen.blit(purp, (screen_width * 1/10 -50, screen_height * 2/4 -130))
    if p13:
        screen.blit(purp, (screen_width * 5/10 -80, screen_height * 2/4 -130))
    #rules
    if rules:
        screen.blit(surface, (screen_width/3, screen_height/3))
        screen.blit(title, (screen_width/2 - 120, sy + 40))
        screen.blit(text1, (sx + 100, sy + 190))
        screen.blit(text, (sx + 60, sy + 120))
    if pp >= 12:
        screen.blit(surface2, (0,0))
        screen.blit(text3, (screen_width/4, screen_height/3 + 40))
    # Update display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)
