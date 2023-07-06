import pygame

from gameCode.itemClass import defaultItem
from gameCode.entityClass import bulletClass

class Ammunition(defaultItem.Item):
    
    def __init__(self, itemName, itemTextureLink, itemIconLink, secondItemType='default', pickingTimeValue=0):
        super().__init__(itemName, itemTextureLink, itemIconLink)
        self.firstItemType = 'ammunition'
        self.secondItemType = secondItemType

        self.pickingTimeValue = pickingTimeValue

        self.stackable = True

    def useMake(self, entity, targets, mouse, spreadingAngleValue, shotingSpeedValue, damageAmountValue, ammoAmountValue):
        for use in range(ammoAmountValue):
            bulletClass.defaultBullet.Bullet(entity=entity, targets=targets, mouse=mouse, spreadingAngleValue=spreadingAngleValue, shotingSpeedValue=shotingSpeedValue, damageAmountValue=damageAmountValue)

    def update(self, entity=None, mouse=None, mouseState=None, keyState=None, dtime=None, TARGET_FPS=None):
        self.existChesk()
        if self.picked:
            pass
        else:
            self.pickingUpdate(dtime)

        
