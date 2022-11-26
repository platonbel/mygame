import pygame
from modules import shapeClass, interfaceClass

class Item():
    
    def __init__(self, itemname=None, iconimage=None, pickingtime=0, amount=1):
        
        if iconimage:
            self.itemicon = iconimage
        else:
            self.itemicon = "src/assets/textures/default_icon.png"
        
        self.itemtexture = None

        self.amount = amount
        self.pickingtime = pickingtime
        self.pickingdelay = 0
        
        self.itemtype = 'default'
        self.itemname = itemname

        self.stackable = True
        self.owner = None
        self.picked = False
        self.exist = True

    def existChesk(self):
        if self.amount <= 0:
            self.__del__()

    def picking(self, dtime):
        if not self.picked:
            self.pickingdelay += dtime
            if self.pickingdelay >= self.pickingtime:
                self.pickingdelay = 0
                self.picked = True

    def update(self, mouse=None, mousestate=None, keystate=None, dtime=None, TARGET_FPS=None):
        self.existChesk()

    def __del__(self):
        self.exist = False


