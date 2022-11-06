
import pygame
from . import defaultRangedWeapon, bulletClass

class PumpShotgun(defaultRangedWeapon.RangedWeapon):

    def __init__(self, iconimage, spreadangle, shotrange, shotspeed, reloadtime, pickingtime, damage, ammo, maxammo):
        super().__init__(iconimage, spreadangle, shotrange, shotspeed, reloadtime, pickingtime, damage, ammo, maxammo)
        self.ammunitiontype = '12/70'
        self.weapontype = 'pumpShotgun'
        
    def attack(self, mouse, mousestate, dtime, TARGET_FPS):
        if mousestate[0] and self.ammo != 0:
            if self.shotdelay == 0:
                if not self.mouseswith['0']:
                    self.ammo -= 1
                    bulletClass.buckshotBullet.Buckshot(owner=self.owner, targets=self.targets, mouse=mouse, spreadangle=self.spreadangle, shotrange=self.shotrange, damage=self.damage)
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

    def reload(self, keystate, dtime, TARGET_FPS):
        if keystate[pygame.K_r]:
            if (not self.reloading) and (not self.shooting) and (self.ammo != self.maxammo):
                if not self.keyswith['K_r']:
                    self.reloading = True
        else:
            self.keyswith['K_r'] = False
        if self.reloading:
            self.reloaddelay += dtime
            if self.reloaddelay >= self.reloadtime*dtime*TARGET_FPS:
                totalammo = self.ammunition + self.ammo
                self.ammo += 1
                self.ammunition = totalammo - self.ammo
                self.owner.inventory[self.ammunitiontype] = self.ammunition
                self.reloaddelay = 0
                self.keyswith['K_r'] = True
                if self.ammo == self.maxammo:
                    self.reloading = False
        else:
            self.reloaddelay = 0
