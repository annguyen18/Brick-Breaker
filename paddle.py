import pygame
from pygame.locals import *

paddleX = 375
paddleY = 615
paddleWidth = 170
paddleHeight = 35


class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        # init sprite class
        super().__init__()

        # image is the surface to be displayed
        self.image = pygame.image.load(
            'paddle.png').convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (170, 35))  # 1438 x 500
        # rect is the rectangle that surrounds the object
        self.rect = self.image.get_rect()
        self.rect.x = paddleX
        self.rect.y = paddleY

    def paddle_input(self, vel):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= vel
            if self.rect.x < 0:
                self.rect.x = 0
        elif keys[pygame.K_RIGHT]:
            self.rect.x += vel
            if self.rect.x > (900-paddleWidth):
                self.rect.x = (900-paddleWidth)
        else:
            pygame.mouse.set_visible(False)
            for event in pygame.event.get():
                mouse_pos = pygame.mouse.get_pos()[0]
                if mouse_pos < paddleWidth/2:
                    self.rect.x = 0
                if self.rect.x > (900-paddleWidth):
                    self.rect.x = (900-paddleWidth)+paddleWidth/2
                self.rect.x = mouse_pos-paddleWidth/2

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))
