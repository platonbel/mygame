
import pygame
from . import defaultRangedWeapon

class Shotgun(defaultRangedWeapon.RangedWeapon):

    def __init__(self, itemname, iconimage, spreadangle, shotrange, shotspeed, reloadtime, pickingtime, damage, bulletamount, ammo, maxammo, ammunitiontype):
        super().__init__(itemname, iconimage, spreadangle, shotrange, shotspeed, reloadtime, pickingtime, damage, bulletamount, ammo, maxammo, ammunitiontype)
        self.weapontype = 'shotgun'
        
    def attack(self, owner, mouse, mousestate, dtime, TARGET_FPS):
        if mousestate[0]:
            if self.shotdelay == 0:
                if not self.mouseswitch['0']:
                    if self.ammo:
                        self.ammunition.use(owner=owner, targets=owner.enemygroup, mouse=mouse, spreadangle=self.spreadangle, shotrange=self.shotrange, damage=self.damage, bulletamount=self.bulletamount)
                        self.ammo -= 1
                        self.shotdelay = (self.shotdelay + dtime*self.shotspeed)
                        self.shooting = True
                        self.reloading = False
                        self.mouseswitch['0'] = True
        else:
            self.shooting = False
            self.mouseswitch['0'] = False
        if self.shotdelay != 0:
            self.shotdelay = (self.shotdelay + dtime*self.shotspeed)
            if self.shotdelay >= TARGET_FPS:
                self.shotdelay = 0
