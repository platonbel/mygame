import pygame

from modules.itemClass import defaultItem

class Weapon(defaultItem.Item):
    
    def __init__(self, iconimage, pickingtime, damage):
        super().__init__(iconimage=iconimage, pickingtime=pickingtime)

        self.damage = damage

        self.itemtype = 'defaultWeapon'
        self.weapontype = 'default'
        
        self.targets = None
        self.mouseswith = {'0': False}

    def attack(self, mouse, mousestate, dtime, TARGET_FPS):
        None

    def update(self, mouse, mousestate, keystate, dtime, TARGET_FPS):
        self.picking(dtime)
        self.attack(mouse, mousestate, dtime, TARGET_FPS)

        
