import pygame
from modules import shapeClass

class Shape(pygame.sprite.Sprite):
    instances = set()

    def __init__(self, image=None, headobject=None, size=(0, 0), position=(0, 0), side=None, color=(0, 0, 0), alpha=255, layer=0):
        Shape.instances.add(self)
        super().__init__()
        self.add(shapeClass.instances.shapeGroup.defaultGroup)
        shapeClass.instances.shapeLayer.defaultLayer.add(self, layer=layer)

        #bind headobject
        self.headobject = headobject

        #render options
        self.position = position
        self.side = side
        self.size = size
        self.color = color
        self.alpha = alpha
        self.hided = False
        if image:
            self.image = pygame.image.load(image).convert_alpha()
        else:
            self.image = pygame.Surface(self.size)
            self.image.fill(self.color)
            self.image.set_alpha(self.alpha)
        self.rect = self.image.get_rect()
        self.moving(self.position)

    def moving(self, position):
        self.position = position
        match self.side:
            case 'topleft':
                self.rect.topleft = self.position
            case 'midtop':
                self.rect.midtop = self.position
            case 'topright':
                self.rect.topright = self.position
            case 'midright':
                self.rect.midright = self.position
            case 'bottomright':
                self.rect.bottomright = self.position
            case 'midbottom':
                self.rect.midbottom = self.position
            case 'bottomleft':
                self.rect.bottomleft = self.position
            case 'midleft':
                self.rect.midleft = self.position
            case 'center':
                self.rect.center = self.position
            case _:
                self.rect.center = self.position

    def sizeedit(self, size):
        self.size = size
        self.image = pygame.Surface(self.size)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.moving(self.position)

    def imageedit(self, image):
        if image:
            self.image = pygame.image.load(image).convert_alpha()
            self.rect = self.image.get_rect()
            self.moving(self.position)
        else:
            self.image = pygame.Surface(self.size)
            self.image.fill(self.color)
            self.image.set_alpha(self.alpha)
            self.rect = self.image.get_rect()
            self.moving(self.position)

    def coloredit(self, color):
        self.color = color
        self.image.fill(self.color)

    def visible(self, hided):
        self.hided = hided
        if self.hided:
            self.image.set_alpha(0)
        else:
            self.image.set_alpha(self.alpha)