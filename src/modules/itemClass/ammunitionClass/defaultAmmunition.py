import pygame

from modules.itemClass import defaultItem

class Ammunition(defaultItem.Item):
    
    def __init__(self, iconimage, ammunitiontype='default'):
        super().__init__(iconimage=iconimage)

        self.itemtype = 'ammunition'
        self.ammunitiontype = ammunitiontype

    def update(self, dtime):
        self.existChesk()
        self.picking(dtime)

        
