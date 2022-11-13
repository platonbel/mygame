import pygame
import math
from modules import entityClass, interfaceClass, textClass, shapeClass

class Indicator():

    def __init__(self, screen):
        self.hided = True
        
        self.itemIndicator = shapeClass.privateShape.Shape(image="src/assets/textures/item_indicator.png", position=(screen.get_width()-30, screen.get_height()-142), side='bottomright', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)

        #self.reloadbar = shapeClass.privateShape.Shape(headobject=self.itemIndecator, size=(224, 24), side='topleft', color=(205, 205, 50), layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)

        self.ammovalue = textClass.privateText.Text(headobject=self.itemIndicator, size=36, side='center', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.ammunitionvalue = textClass.privateText.Text(headobject=self.itemIndicator, size=36, side='center', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.ammunitiontypevalue = textClass.privateText.Text(headobject=self.itemIndicator, size=36, side='center', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
    
        self.ammovalue.moving((self.ammovalue.headobject.rect.topleft[0]+332, self.ammovalue.headobject.rect.topleft[1]+52))
        self.ammunitionvalue.moving((self.ammovalue.headobject.rect.topleft[0]+228, self.ammovalue.headobject.rect.topleft[1]+78))
        self.ammunitiontypevalue.moving((self.ammovalue.headobject.rect.topleft[0]+228, self.ammovalue.headobject.rect.topleft[1]+26))

    def indicatorrender(self, player):
        if player.item != None:

            if player.item.itemtype == 'rangedWeapon':
                ammoratio = player.item.ammo
                maxammoratio = player.item.maxammo
                key, value = player.inventory.founditem(player.item.ammunitiontype, 'ammunitiontype')
                ammunitionratio = value.amount if value else 0
                ammunitiontyperatio = player.item.ammunitiontype + ' к.'
                if player.item.reloading:
                    reloadratio = player.item.reloaddelay / player.item.reloadtime
                else:
                    reloadratio = 0

            else:
                reloadratio = 0
                ammoratio = 0
                maxammoratio = 0
                ammunitionratio = 0
                ammunitiontyperatio = None
                
            self.hided = False

            self.ammunitionvalue.textedit(f'{ammunitionratio}', color=(225, 225, 255))
            self.ammunitiontypevalue.textedit(f'{ammunitiontyperatio}', color=(225, 225, 255))
            self.ammovalue.textedit(f'{ammoratio}/{maxammoratio}', color=(225, 225, 255))

        else:
            ammoratio = 0
            maxammoratio = 0
            ammunitionratio = 0
            ammunitiontyperatio = None
            self.hided = True

        self.itemIndicator.visible(self.hided)
        self.ammovalue.visible(self.hided)
        self.ammunitionvalue.visible(self.hided)
        self.ammunitiontypevalue.visible(self.hided)

