import pygame
from modules import shapeClass, textClass, interfaceClass

class Icon():
    instances = set()

    def __init__(self, position=(0, 0)):
        Icon.instances.add(self)
        self.itemicon = shapeClass.privateShape.Shape(side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.itemamount = textClass.privateText.Text(side='bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        
        self.position = position
        self.hided = False
        self.moving(self.position)

    def iconRender(self, item):
        if item:
            self.itemicon.imageedit(item.itemicon)
            match item.itemtype:
                case 'ammunition':
                    self.itemamount.textedit(str(item.amount), (0, 0, 0))
                case _:
                    self.itemamount.textedit(None, (0, 0, 0))
        else:
            self.itemicon.imageedit("src/assets/textures/empty_icon.png")
            self.itemamount.textedit(None, (0, 0, 0))

    def moving(self, position):
        self.position = position
        self.itemicon.moving(self.position)
        self.itemamount.moving((self.itemicon.position[0]+32, self.itemicon.position[1]+32))

    def visible(self, hided):
        self.hided = hided
        self.itemicon.visible(self.hided)
        self.itemamount.visible(self.hided)