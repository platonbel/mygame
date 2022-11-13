
import pygame
import math
from . import defaultRangedWeapon

class AssaultRifle(defaultRangedWeapon.RangedWeapon):

    def __init__(self, iconimage, spreadangle, shotrange, shotspeed, reloadtime, pickingtime, damage, bulletamount, ammo, maxammo):
        super().__init__(iconimage, spreadangle, shotrange, shotspeed, reloadtime, pickingtime, damage, bulletamount, ammo, maxammo)
        self.ammunitiontype = '7.62'
        self.weapontype = 'assaultRifle'
    def attack(self, mouse, mousestate, dtime, TARGET_FPS):

        if self.picked:
            if mousestate[0]:
                if self.shotdelay == 0:
                    self.mouseswith['0'] = False
                    if not self.mouseswith['0']:
                        if self.ammo:
                            self.ammunition.use(owner=self.owner, targets=self.targets, mouse=mouse, spreadangle=self.spreadangle, shotrange=self.shotrange, damage=self.damage, bulletamount=self.bulletamount)
                            self.ammo -= 1
                            self.shooting = True
                            self.reloading = False
                self.shotdelay = (self.shotdelay + dtime*self.shotspeed)
                if self.shotdelay >= TARGET_FPS: 
                    self.shotdelay = 0
            else:
                self.shooting = False
                self.mouseswith['0'] = True
                self.shotdelay = 0





