
import pygame
from . import defaultRangedWeapon

class Pistol(defaultRangedWeapon.RangedWeapon):

    def __init__(self, iconimage, spreadangle, shotrange, shotspeed, reloadtime, pickingtime, damage, bulletamount, ammo, maxammo):
        super().__init__(iconimage, spreadangle, shotrange, shotspeed, reloadtime, pickingtime, damage, bulletamount, ammo, maxammo)
        self.ammunitiontype = '9x18'
        self.weapontype = 'pistol'

    def attack(self, mouse, mousestate, dtime, TARGET_FPS):
        if self.picked:
            if mousestate[0]:
                if self.shotdelay == 0:
                    if not self.mouseswith['0']:
                        if self.ammo:
                            self.ammunition.use(owner=self.owner, targets=self.targets, mouse=mouse, spreadangle=self.spreadangle, shotrange=self.shotrange, damage=self.damage, bulletamount=self.bulletamount)
                            self.ammo -= 1
                            self.shotdelay = (self.shotdelay + dtime*self.shotspeed)
                            self.shooting = True
                            self.reloading = False
                            self.mouseswith['0'] = True
            else:
                self.shooting = False
                self.mouseswith['0'] = False
            if self.shotdelay != 0:
                self.shotdelay = (self.shotdelay + dtime*self.shotspeed)
                if self.shotdelay >= TARGET_FPS:
                    self.shotdelay = 0
