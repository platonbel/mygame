import pygame
import math
from modules.weaponClass import bulletClass

class Weapon():
    
    def __init__(self, spreadangle=0, shotrange=0, shotspeed=0, damage=0, ammo=math.inf, maxammo=math.inf, ammunition=math.inf, shooter=None, targets=None):
        self.spreadangle = spreadangle
        self.shotrange = shotrange
        self.shotspeed = shotspeed
        self.delay = 0 #
        self.damage = damage
        self.ammo = ammo
        self.maxammo = maxammo
        self.ammunition = ammunition
        self.shooter = shooter
        self.targets = targets
        self.weapontype = 'default'
        self.keyswith = {'K_r': False}
        self.mouseswith = {'0': False}

    def attack(self, mouse, mousestate, dtime, TARGET_FPS):
        if mousestate[0] and self.ammo != 0:
            if self.mouseswith['0']:
                self.ammo -= 1
                bulletClass.defaultBullet.Bullet(shooter=self.shooter, targets=self.targets, mouse=mouse, spreadangle=self.spreadangle, shotrange=self.shotrange, damage=self.damage)
                self.mouseswith['0'] = False
        else:
            self.mouseswith['0'] = True
        
    def reload(self, keystate):
        if keystate[pygame.K_r]:
            if self.ammo != self.maxammo:
                if self.keyswith['K_r']:
                    totalammo = self.ammunition + self.ammo
                    self.ammo = min(totalammo, self.maxammo)
                    self.ammunition = totalammo - self.ammo
                self.keyswith['K_r'] = True
        else:
            self.keyswith['K_r'] = False
