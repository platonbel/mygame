import math
from . import defaultIndicatorClass
from gameCode import interfaceClass, textClass, shapeClass, functions

class Indicator(defaultIndicatorClass.Indicator):

    def __init__(self):
        self.hided = True
        self.ammoValue = 0
        self.ammunitionValue = 0
        self.ammunitionTypeValue = 0
        self.itemIconLink = None

        self.itemIndicatorBackground = shapeClass.defaultShape.Shape(image="src/assets/textures/item_indicator.png", layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.ammoText = textClass.defaultText.Text(headobject=self.itemIndicatorBackground, size=36, side='center', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.ammunitionText = textClass.defaultText.Text(headobject=self.itemIndicatorBackground, size=36, side='center', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.ammunitionTypeText = textClass.defaultText.Text(headobject=self.itemIndicatorBackground, size=36, side='center', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.itemIcon = shapeClass.defaultShape.Shape(image="src/assets/textures/default_icon.png", headobject=self.itemIndicatorBackground, side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)

    def valueUpdate(self, entity):
        if entity.inventory.item:
            match entity.inventory.item.itemtype:
                case 'rangedWeapon':
                    self.ammoValue = entity.inventory.item.ammo
                    self.maxAmmoValue = entity.inventory.item.maxammo
                    aviableAmmunition = functions.founditems(entity.inventory.inventoryslots, entity.inventory.item.ammunition)
                    self.ammunitionValue = sum([value.amount for value in aviableAmmunition.values()]) if aviableAmmunition else 0
                    self.ammunitionTypeValue = entity.inventory.item.ammunitiontype
                    self.itemIconLink = entity.inventory.item.itemicon
                case _:
                    self.ammoValue = 0
                    self.maxAmmoValue = 0
                    self.ammunitionValue = entity.inventory.item.amount
                    self.ammunitionTypeValue = entity.inventory.item.itemtype
                    self.itemIconLink = entity.inventory.item.itemicon
        else:
            self.ammoValue = 0
            self.maxAmmoValue = 0
            self.ammunitionValue = 0
            self.ammunitionTypeValue = 0
            self.itemIconLink = None

    def imageUpdate(self):
        self.ammoText.textedit(f'{self.ammoValue}/{self.maxAmmoValue}', color=(225, 225, 255))
        self.ammunitionText.textedit(f'{self.ammunitionValue}', color=(225, 225, 255))
        self.ammunitionTypeText.textedit(f'{self.ammunitionTypeValue}', color=(225, 225, 255))
        self.itemIcon.imageedit(self.itemIconLink)


    def positionUpdate(self, position, side):
        self.position = position
        self.side = side
        self.itemIndicatorBackground.moving(self.position, self.side)
        self.ammoText.moving((self.ammoText.headobject.get_position(side='topleft')[0]+364, self.ammoText.headobject.get_position(side='topleft')[1]+52), side='topleft')
        self.ammunitionText.moving((self.ammunitionText.headobject.get_position(side='topleft')[0]+260, self.ammunitionText.headobject.get_position(side='topleft')[1]+78), side='topleft')
        self.ammunitionTypeText.moving((self.ammunitionTypeText.headobject.get_position(side='topleft')[0]+260, self.ammunitionTypeText.headobject.get_position(side='topleft')[1]+26), side='topleft')
        self.itemIcon.moving((self.itemIcon.headobject.get_position(side='topleft')[0]+104, self.itemIcon.headobject.get_position(side='topleft')[1]+52), side='topleft')
    
    def visibleUpdate(self, entity):
        self.hided = False if entity.inventory.item else True
        self.itemIndicatorBackground.visible(self.hided)
        self.ammoText.visible(self.hided)
        self.ammunitionText.visible(self.hided)
        self.ammunitionTypeText.visible(self.hided)