import pygame
from modules import textClass

class Text(pygame.sprite.Sprite):
    instances = set()

    def __init__(self, text=None, size=24, color=(0, 0, 0), position=(0, 0), side=None, layer=0, private=None):
        Text.instances.add(self)
        super().__init__()
        self.add(textClass.instances.textGroup.defaultGroup)
        private.add(self, layer=layer)
            
        #creating text label
        self.font = pygame.font.SysFont('arial', size)
        self.image = self.font.render(text, True, color)
        self.rect = self.image.get_rect()

        #set here static position
        self.position = position
        self.side = side

        #render options
        self.hided = False
    
    def textedit(self, text, color):
        self.image = self.font.render(text, True, color)
        self.rect = self.image.get_rect()

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
            self.image.set_alpha(255)

    def update(self):
        self.visible()
        self.moving()

    def __del__(self):
        self.kill()