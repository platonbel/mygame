import pygame
from gameCode import chhh, interfaceClass

class Icon():
    instances = 0
    def __init__(self, position=(0, 0), side=None):
        Icon.instances += 1
        self.hitBox = chhh.defaultHitBox.HitBox(size=(88, 88), layer=0, hitBoxGroup=None, hitBoxLayer=None)
        self.iconImage = chhh.defaultShape.Shape(name='iconImage'+str(Icon.instances), imageLink="src/assets/textures/empty_icon.png", side='center', mainObjectLink=self.hitBox, layer=2, shapeGroup=interfaceClass.instances.iconGroup.iconImageGroup, shapeLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.iconText = chhh.defaultTitle.Text(name='iconText'+str(Icon.instances), side='bottomright', mainObjectLink=self.hitBox, layer=3, shapeGroup=interfaceClass.instances.iconGroup.iconTextGroup, shapeLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        
        self.visible = True
        self.position_edit(position, side)

    def update(self, item):
        if item:
            self.iconImage.image_edit(item.itemIconLink)
            self.iconText.text_edit(str(item.amountValue) if item.stackable else None)
        else:
            self.iconImage.image_edit("src/assets/textures/empty_icon.png")
            self.iconText.text_edit(None)

    def position_edit(self, position=None, side=None):
        self.hitBox.position_edit(position=position, side=side)
        self.iconImage.subPosition_edit(position=(0, 0), side='center', subSide='center')
        self.iconText.subPosition_edit(position=(-12, -12), side='bottomright', subSide='bottomright')

    def visible_edit(self, visible=True):
        self.visible = visible
        self.iconImage.visible_edit(self.visible)
        self.iconText.visible_edit(self.visible)

    def get_position(self, side=None):
        match side:
            case 'topleft':
                return self.hitBox.rect.topleft
            case 'midtop':
                return self.hitBox.rect.midtop
            case 'topright':
                return self.hitBox.rect.topright
            case 'midright':
                return self.hitBox.rect.midright
            case 'bottomright':
                return self.hitBox.rect.bottomright
            case 'midbottom':
                return self.hitBox.rect.midbottom
            case 'bottomleft':
                return self.hitBox.rect.bottomleft
            case 'midleft':
                return self.hitBox.rect.midleft
            case 'center':
                return self.hitBox.rect.center
            case _:
                return self.hitBox.rect.topleft
