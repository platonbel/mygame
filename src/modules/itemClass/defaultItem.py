import pygame
from modules import shapeClass, interfaceClass

class Item():
    
    def __init__(self, iconimage=None, pickingtime=0):
        
        if iconimage:
            self.itemicon = iconimage
        else:
            self.itemicon = "src/assets/textures/default_icon.png"
        
        self.itemtexture = None

        self.pickingtime = pickingtime
        self.pickingdelay = 0
        
        self.itemtype = 'default'

        self.owner = None
        self.picked = False
        
    def picking(self, dtime):
        if not self.picked:
            self.pickingdelay += dtime
            if self.pickingdelay >= self.pickingtime:
                self.pickingdelay = 0
                self.picked = True

    def update(self, mouse, mousestate, keystate, dtime, TARGET_FPS):
        self.picking(dtime)

