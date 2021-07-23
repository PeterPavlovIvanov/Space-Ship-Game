import pygame
import random
import math

pygame.init()

# Screen ----------------------------------------------------------------------------------
screen = pygame.display.set_mode((800, 600))

# Title and Icon ----------------------------------------------------------------------------------
pygame.display.set_caption("Snake")
icon = pygame.image.load('Icons/Ship.png')
pygame.display.set_icon(icon)

# Clock ----------------------------------------------------------------------------------
clock = pygame.time.Clock()

# colors ----------------------------------------------------------------------------------
white = (255, 255, 255)
black = (0, 0, 0)
green = (255, 0, 0)

# Player ----------------------------------------------------------------------------------
playerImg = pygame.image.load('Icons/Player.png')
x_player = 368
y_player = 500
x_player_move_left = 0
x_player_move_right = 0
y_player_move_up = 0
y_player_move_down = 0
player_tilt = 0


def player(x, y, player_tilt):
    player_img_cpy = pygame.transform.rotate(playerImg, player_tilt)
    screen.blit(player_img_cpy, (x - (player_img_cpy.get_width() / 2), y - (player_img_cpy.get_height() / 2)))


# Asteroid ----------------------------------------------------------------------------------
asteroidImg = pygame.image.load('Icons/Asteroid.png')
x_asteroid = random.randint(32, 768)
y_asteroid = -32
x_asteroid_move_left = 0.1
x_asteroid_move_right = 0.1
y_asteroid_move_up = 0.1
y_asteroid_move_down = 0.1
angle_asteroid = 0


def asteroid(x, y, angle):
    img_cpy = pygame.transform.rotate(asteroidImg, angle)
    screen.blit(img_cpy, (x - (img_cpy.get_width() / 2), y - (img_cpy.get_height() / 2)))


# Background Stars ----------------------------------------------------------------------------------
whiteDotImg = pygame.image.load('Icons/WhiteDot.png')
y_start = -5
y_end = 605
y_white_dot = -4
x_white_dot = 330
dots_list = [0] * 300 # Keeps x, y, speed of a dot for every 3 indexes (total 100 dots)

number = 0
while number < 300:
    dots_list[number] = random.randint(0, 800)
    dots_list[number + 1] = random.randint(-605, -5)
    dots_list[number + 2] = random.randint(1, 10)
    number += 3


def white_dot(x, y, start, end, speed):
    y += speed

    if y > end:
        y -= 604
        x = random.randint(0, 800)

    screen.blit(whiteDotImg, (x, y))
    return x, y


def background_white_dots():
    num = 0
    while num < len(dots_list):
        dots_list[num], dots_list[num + 1] = white_dot(dots_list[num], dots_list[num + 1], y_start, y_end, dots_list[num + 2] / 100)
        num += 3


# Game loop ----------------------------------------------------------------------------------
applicationProcess = True
while applicationProcess:

    # Draw Background
    screen.fill(black)
    background_white_dots()

    # Draw Player
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            applicationProcess = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_player_move_left += 0.18
                player_tilt += math.pi
            if event.key == pygame.K_RIGHT:
                x_player_move_right += 0.18
                player_tilt += -math.pi
            if event.key == pygame.K_UP:
                y_player_move_up += 0.18
            if event.key == pygame.K_DOWN:
                y_player_move_down += 0.18

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                x_player_move_left = 0
                player_tilt += -math.pi
            if event.key == pygame.K_RIGHT:
                x_player_move_right = 0
                player_tilt += math.pi
            if event.key == pygame.K_UP:
                y_player_move_up = 0
            if event.key == pygame.K_DOWN:
                y_player_move_down = 0
            if event.key == pygame.K_LEFT and event.key == pygame.K_RIGHT:
                player_tilt = 0

    x_player -= x_player_move_left
    x_player += x_player_move_right
    y_player -= y_player_move_up
    y_player += y_player_move_down

    if x_player <= 1:
        x_player = 1
    elif x_player >= 735:
        x_player = 735

    if y_player <= 1:
        y_player = 1
    elif y_player >= 535:
        y_player = 535

    player(x_player, y_player, player_tilt)

    # Draw Asteroids
    angle_asteroid += 0.05
    y_asteroid += y_asteroid_move_down

    if y_asteroid >= 632:
        y_asteroid = -32
        x_asteroid = random.randint((int)(x_player - 200) if x_player - 200 > 32 else 32,
                                    (int)(x_player + 200) if x_player + 200 < 768 else 768)

    asteroid(x_asteroid, y_asteroid, angle_asteroid)

    pygame.display.update()
