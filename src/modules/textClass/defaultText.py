import pygame
from modules import textClass

class Text(pygame.sprite.Sprite):
    instances = set()

    def __init__(self, text=None, headobject=None, size=36, color=(0, 0, 0), position=(0, 0), side=None, layer=0):
        Text.instances.add(self)
        super().__init__()
        self.add(textClass.instances.textGroup.defaultGroup)
        textClass.instances.textLayer.defaultLayer.add(self, layer=layer)
            
        #creating text label
        self.font = pygame.font.SysFont('neo sans pro', size)
        self.image = self.font.render(text, True, color)
        self.rect = self.image.get_rect()

        #set here static position
        self.position = position
        self.side = side

        #bind headobject
        self.headobject = headobject

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