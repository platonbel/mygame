import pygame

from modules.itemClass import defaultItem
from modules.entityClass import bulletClass

class Ammunition(defaultItem.Item):
    
    def __init__(self, iconimage, ammunitiontype='default'):
        super().__init__(iconimage=iconimage)

        self.itemtype = 'ammunition'
        self.ammunitiontype = ammunitiontype

    def use(self, owner, targets, mouse, spreadangle, shotrange, damage, bulletamount):
        for i in range(bulletamount):
            bulletClass.defaultBullet.Bullet(owner=owner, targets=targets, mouse=mouse, spreadangle=spreadangle, shotrange=shotrange, damage=damage)

    def update(self, dtime):
        self.existChesk()
        self.picking(dtime)

        
