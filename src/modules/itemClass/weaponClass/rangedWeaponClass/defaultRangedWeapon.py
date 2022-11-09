import pygame
import math
from modules.itemClass.weaponClass import defaultWeapon
from modules.entityClass import bulletClass

class RangedWeapon(defaultWeapon.Weapon):
    
    def __init__(self, iconimage=None, spreadangle=0, shotrange=0, shotspeed=0, reloadtime=0, pickingtime=0, damage=0, ammo=math.inf, maxammo=math.inf):
        super().__init__(iconimage=iconimage, pickingtime=pickingtime, damage=damage)

        self.spreadangle = spreadangle
        self.shotrange = shotrange
        self.shotspeed = shotspeed
        self.reloadtime = reloadtime

        self.shotdelay = 0 
        self.reloaddelay = 0

        self.itemtype = 'rangedWeapon'
        self.weapontype = 'default'
        self.ammunitiontype = 'default'

        self.ammo = ammo
        self.maxammo = maxammo
        self.ammunition = 0

        self.shooting = False
        self.reloading = False

        self.keyswith = {'K_r': False}
        self.mouseswith = {'0': False}

    def picking(self, dtime):
        if not self.picked:
            self.pickingdelay += dtime
            if self.pickingdelay >= self.pickingtime:
                self.pickingdelay = 0
                self.picked = True

    def attack(self, mouse, mousestate, dtime, TARGET_FPS):
        if self.picked:
            if mousestate[0] and self.ammo != 0:
                if not self.mouseswith['0']:
                    self.ammo -= 1
                    bulletClass.defaultBullet.Bullet(shooter=self.owner, targets=self.targets, mouse=mouse, spreadangle=self.spreadangle, shotrange=self.shotrange, damage=self.damage)
                    self.shooting = True
                    self.mouseswith['0'] = True
            else:
                self.shooting = False
                self.mouseswith['0'] = False
            
        
    def reload(self, keystate, dtime, TARGET_FPS):
        if self.picked:
            if keystate[pygame.K_r]:
                if (not self.reloading) and (not self.shooting) and (self.ammo != self.maxammo):
                    if not self.keyswith['K_r']:
                        self.reloading = True
            else:
                self.keyswith['K_r'] = False

            if self.reloading:
                self.reloaddelay += dtime
                if self.reloaddelay >= self.reloadtime * dtime * TARGET_FPS:
                    self.reloaddelay = 0
                    key, value = self.owner.inventory.founditem(self.ammunitiontype, 'ammunitiontype')
                    if value:
                        totalammo = self.ammo + value.amount
                        self.ammo = min(totalammo, self.maxammo)
                        self.owner.inventory.inventoryslots[key].amount -= self.ammo
                    self.reloading = False
                    self.keyswith['K_r'] = True
            else:
                self.reloaddelay = 0

    def update(self, mouse, mousestate, keystate, dtime, TARGET_FPS):
        self.existChesk()
        self.reload(keystate, dtime, TARGET_FPS)
        self.attack(mouse, mousestate, dtime, TARGET_FPS)

        
