import pygame

from modules.itemClass import defaultItem

class Weapon(defaultItem.Item):
    
    def __init__(self, iconimage, pickingtime):
        super().__init__(iconimage=iconimage, pickingtime=pickingtime)

        self.itemtype = 'defaultWeapon'
        self.weapontype = 'default'
        
        self.targets = None
        self.mouseswith = {'0': False}

    def attack(self, mouse, mousestate, dtime, TARGET_FPS):
        if self.picked:
            None

    def update(self, mouse, mousestate, keystate, dtime, TARGET_FPS):
        self.existChesk()
        self.attack(mouse, mousestate, dtime, TARGET_FPS)

        
