import pygame
from random import randint
from random import randint
from time import sleep
ball_size = 40

#  self.rect.x = 450
#         self.rect.y = 400
s = []


class Ball(pygame.sprite.Sprite):
    def __init__(self, image):
        # Call the parent class (Sprite) constructor
        super().__init__()

        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (ball_size, ball_size))
        self.rect = self.image.get_rect()
        # velocity of x and y axis
        # a = randint(-3, 6)
        # b = randint(3, 8)
        # self.velocity = []
        # self.velocity.append(a)
        # self.velocity.append(b)
        self.velocity = [7, 9]
        s.append(7)
        s.append(9)

    def spawn(self):
        self.rect.x = 375
        self.rect.y = 615-25
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.rect.x += s[0]
            self.rect.y += s[1]

    def update(self, paddle):

        collide = pygame.Rect.colliderect(self.rect, paddle)
        if collide:
            self.velocity[1] *= -1

        # if the ball touches left/right border
        if self.rect.left < 0 or self.rect.right >= 900:
            self.velocity[0] *= -1

        # if the ball touches top border
        if self.rect.top < 0:
            self.velocity[1] *= -1

        # if the ball go over bottom border
        # if self.rect.bottom >= 700:
        #     spawn()

        # self.rect.move_ip(self.velocity)

    # def update(self):
    #     self.rect.x += self.velocity[0]
    #     self.rect.y += self.velocity[1]
    #     print("UPDATE: {}   {}".format(self.rect.x, self.rect.y))

    # def bounce(self):
    #     self.velocity[0] = -self.velocity[0]
    #     self.velocity[1] = randint(-1, 3)
    #     print("BOUNCE: {}   {}".format(self.velocity[0], self.velocity[1]))

    def draw(self, window):
        window.blit(self.image, (self.rect.x, self.rect.y))
