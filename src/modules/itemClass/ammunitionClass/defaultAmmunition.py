import pygame

from modules.itemClass import defaultItem
from modules.entityClass import bulletClass

class Ammunition(defaultItem.Item):
    
    def __init__(self, itemname, iconimage, ammunitiontype='default', pickingtime=0):
        super().__init__(itemname, iconimage, pickingtime)

        self.itemtype = 'ammunition'
        self.ammunitiontype = ammunitiontype

        self.stackable = True
    def use(self, owner, targets, mouse, spreadangle, shotrange, damage, bulletamount):
        for i in range(bulletamount):
            bulletClass.defaultBullet.Bullet(owner=owner, targets=targets, mouse=mouse, spreadangle=spreadangle, shotrange=shotrange, damage=damage)

    def update(self):
        self.existChesk()

        
