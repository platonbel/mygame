import pygame
from gameCode import chhh, interfaceClass

class Cursor():
    def __init__(self):
        self.hitBox = chhh.defaultHitBox.HitBox(size=(24, 32), layer=0, hitBoxGroup=None, hitBoxLayer=None)
        self.cursorImage = chhh.defaultShape.Shape(name='cursor', imageLink="src/assets/textures/cursor_0.png", position=(0, 0), side='topleft', mainObjectLink=self.hitBox, layer=7, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        pygame.mouse.set_visible(False)

    def update(self, mouse, mouseState):
        self.hitBox.position_edit(position=mouse, side='topleft')
        self.cursorImage.subPosition_edit(position=(0, 0), side='topleft', subSide='topleft')
        if mouseState[0]:
            self.cursorImage.image_edit("src/assets/textures/cursor_1.png")
        else:
            self.cursorImage.image_edit("src/assets/textures/cursor_0.png")