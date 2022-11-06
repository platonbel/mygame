
import pygame
from . import defaultRangedWeapon, bulletClass

class Pistol(defaultRangedWeapon.RangedWeapon):

    def __init__(self, iconimage, spreadangle, shotrange, shotspeed, reloadtime, pickingtime, damage, ammo, maxammo):
        super().__init__(iconimage, spreadangle, shotrange, shotspeed, reloadtime, pickingtime, damage, ammo, maxammo)
        self.ammunitiontype = '9x18'
        self.weapontype = 'pistol'

    def attack(self, mouse, mousestate, dtime, TARGET_FPS):
        if mousestate[0] and self.ammo != 0:
            if self.shotdelay == 0:
                if not self.mouseswith['0']:
                    self.ammo -= 1
                    bulletClass.defaultBullet.Bullet(owner=self.owner, targets=self.targets, mouse=mouse, spreadangle=self.spreadangle, shotrange=self.shotrange, damage=self.damage)
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
