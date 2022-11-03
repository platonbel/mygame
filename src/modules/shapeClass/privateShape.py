import pygame
from modules import shapeClass

class Shape(pygame.sprite.Sprite):
    instances = set()

    def __init__(self, size=(0, 0), position=(0, 0), side=None, color=(0, 0, 0), alpha=255, layer=0, private=None):
        Shape.instances.add(self)
        super().__init__()
        self.add(shapeClass.instances.shapeGroup.defaultGroup)
        private.add(self, layer=layer)

        #creating sprite
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.image.set_alpha(alpha)
        self.rect = self.image.get_rect()

        #set here static position
        self.position = position
        self.side = side

        #render options
        self.hided = False
        self.alpha = alpha

    def moving(self):
        #set position
        match self.side:
            case 'topleft':
                self.rect.topleft = self.position
            case 'top':
                self.rect.top = self.position
            case 'topright':
                self.rect.topright = self.position
            case 'right':
                self.rect.right = self.position
            case 'bottomright':
                self.rect.bottomright = self.position
            case 'bottom':
                self.rect.bottom = self.position
            case 'bottomleft':
                self.rect.bottomleft = self.position
            case 'left':
                self.rect.left = self.position
            case 'center':
                self.rect.center = self.position
            case _:
                self.rect.center = self.position

    def visible(self):
        #displaying the sprite if not hided
        if self.hided:
            self.image.set_alpha(0)
        else:
            self.image.set_alpha(self.alpha)

    def update(self):
        self.moving()
        self.visible()

