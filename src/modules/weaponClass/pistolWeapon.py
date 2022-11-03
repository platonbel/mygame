
import pygame
from modules.weaponClass import bulletClass, defaultWeapon

class Pistol(defaultWeapon.Weapon):

    def __init__(self, spreadangle, shotrange, shotspeed, damage, ammo, maxammo, ammunition, shooter, targets):
        super().__init__(spreadangle, shotrange, shotspeed, damage, ammo, maxammo, ammunition, shooter, targets)
        self.weapontype = 'pistol'

    def attack(self, mouse, mousestate, dtime, TARGET_FPS):
        if mousestate[0] and self.ammo != 0:
            if self.delay == 0:
                if self.mouseswith['0']:
                    self.ammo -= 1
                    bulletClass.defaultBullet.Bullet(shooter=self.shooter, targets=self.targets, mouse=mouse, spreadangle=self.spreadangle, shotrange=self.shotrange, damage=self.damage)
                    self.mouseswith['0'] = False
                    self.delay = (self.delay + dtime*self.shotspeed)
        else:
            self.mouseswith['0'] = True
        if self.delay != 0:
            self.delay = (self.delay + dtime*self.shotspeed)
            if self.delay >= TARGET_FPS:
                self.delay = 0
