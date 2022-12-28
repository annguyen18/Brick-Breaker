import pygame
from PIL import Image

brick_size = 50
size = []


class Brick(pygame.sprite.Sprite):
    def __init__(self, image):
        # Call the parent class (Sprite) constructor
        super().__init__()
        ratio = Image.open(image)
        w, h = ratio.size
        size.append(w)
        size.append(h)
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(
            self.image, (brick_size*(w/h), brick_size))
        self.rect = self.image.get_rect()

    def draw(self, window, x, y):
        window.blit(self.image, (x, y))

    def getWidth(self):
        return brick_size*(size[0]/size[1])

    def getHeight(self):
        return brick_size
