import pygame
from modules import shapeClass

class Shape(pygame.sprite.Sprite):
    instances = set()

    def __init__(self, image=None, headobject=None, size=(0, 0), position=(0, 0), side=None, color=(0, 0, 0), alpha=255, layer=0, privateLayer=None):
        Shape.instances.add(self)
        super().__init__()
        self.add(shapeClass.instances.shapeGroup.defaultGroup)
        privateLayer.add(self, layer=layer)

        #set here static position
        self.position = position
        self.side = side

        #bind headobject
        self.headobject = headobject

        #render options
        self.firstsize = size
        self.firstcolor = color
        self.firstimage = pygame.image.load(image).convert_alpha() if image else None
        self.firstalpha = alpha
        self.hided = False

        #creating sprite
        if not self.firstimage: 
            self.image = pygame.Surface(self.firstsize)
            self.image.fill(self.firstcolor)
            self.image.set_alpha(self.firstalpha)
        else:
            self.image = self.firstimage
        self.rect = self.image.get_rect()

    def moving(self):
        #set position
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
        #changing the sprite size
        self.image = pygame.Surface(size)
        self.image.fill(self.firstcolor)
        self.rect = self.image.get_rect()

    def imageedit(self, image):
        if image:
            self.image = pygame.image.load(image).convert_alpha()
            self.rect = self.image.get_rect()
        else:
            self.image = pygame.Surface(self.firstsize)
            self.image.fill(self.firstcolor)
            self.image.set_alpha(self.firstalpha)
            self.rect = self.image.get_rect()

    def coloredit(self, color):
        self.image.fill(color)

    def visible(self):
        #displaying the sprite if not hided
        if self.hided:
            self.image.set_alpha(0)
        else:
            self.image.set_alpha(self.firstalpha)

    def update(self):
        self.moving()
        self.visible()

