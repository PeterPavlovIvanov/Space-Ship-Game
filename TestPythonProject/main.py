import pygame

pygame.init()

# Screen
screen = pygame.display.set_mode((800, 600))


# Title and Icon
pygame.display.set_caption("Snake")
icon = pygame.image.load('Icons/Ship.png')
pygame.display.set_icon(icon)


# colors
white = (255, 255, 255)
black = (0, 0, 0)
green = (255, 0, 0)


# Game variables
x_player = 368
y_player = 500
x_player_move_left = 0
x_player_move_right = 0
y_player_move_up = 0
y_player_move_down = 0


# Player
playerImg = pygame.image.load('Icons/Player.png')

def player(x, y):
    screen.blit(playerImg, (x, y))


# Game loop
applicationProcess = True
while applicationProcess:
    screen.fill(black)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            applicationProcess = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_player_move_left += 0.3
            if event.key == pygame.K_RIGHT:
                x_player_move_right += 0.3
            if event.key == pygame.K_UP:
                y_player_move_up += 0.3
            if event.key == pygame.K_DOWN:
                y_player_move_down += 0.3

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_player_move_left = 0
            if event.key == pygame.K_RIGHT:
                x_player_move_right = 0
            if event.key == pygame.K_UP:
                y_player_move_up = 0
            if event.key == pygame.K_DOWN:
                y_player_move_down = 0

    x_player -= x_player_move_left
    x_player += x_player_move_right
    y_player -= y_player_move_up
    y_player += y_player_move_down
    player(x_player, y_player)

    pygame.display.update()