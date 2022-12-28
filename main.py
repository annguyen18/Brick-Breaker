import pygame
import sys
import os
from random import choice
from paddle import Paddle
from ball import Ball
from brick import Brick
from levels import *

pygame.init()

WIDTH = 1000
HEIGHT = 700
clock = pygame.time.Clock()
window = pygame.display.set_mode((WIDTH, HEIGHT))   # set a window of 900 x 00
pygame.display.set_caption("Brick Breaker by")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)
bg = pygame.image.load('background2.png')
bg = pygame.transform.scale(bg, (1260, 700))


paddle = Paddle()
ball = Ball("assets/PNG/Round (outline)/chick.png")

animal_list = os.listdir('assets/PNG/Square')

random_animal = choice(animal_list)
# brick = Brick("assets/PNG/Square (outline)/" + (random_animal))


def setup_level():
    x_gap = 50

    for row_index, row in enumerate(level_1):
        y_gap = 30
        for animal in row:
            brick = Brick("assets/PNG/Square (outline)/" +
                          animal_dict[str(animal)] + ".png")
            # print("row {}: {}".format(row_index, i))
            brick.draw(window, y_gap, row_index+x_gap)
            y_gap += brick.getWidth()+10
        x_gap += brick.getHeight() + 10


def setup():
    window.blit(bg, (0, 0))
    paddle.paddle_input(10)
    paddle.draw(window)
    # ball.update(paddle)
    # ball.draw(window)
    setup_level()
    clock.tick(60)
    pygame.display.update()


def start_game():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        setup()
    pygame.quit()


start_game()
