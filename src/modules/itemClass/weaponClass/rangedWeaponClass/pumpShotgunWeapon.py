
import pygame
from modules import functions
from . import defaultRangedWeapon

class PumpShotgun(defaultRangedWeapon.RangedWeapon):

    def __init__(self, itemname, iconimage, spreadangle, shotrange, shotspeed, reloadtime, pickingtime, damage, bulletamount, ammo, maxammo, ammunitiontype):
        super().__init__(itemname, iconimage, spreadangle, shotrange, shotspeed, reloadtime, pickingtime, damage, bulletamount, ammo, maxammo, ammunitiontype)
        self.weapontype = 'pumpShotgun'
        
    def attack(self, owner, mouse, mousestate, dtime, TARGET_FPS):
        if self.picked:
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

    def reload(self, owner, keystate, dtime, TARGET_FPS):
        if not self.reloading:
            if keystate[pygame.K_r]:
                if not self.keyswitch['K_r']:
                    if (not self.reloading) and (not self.shooting) and (self.ammo != self.maxammo):
                        self.reloading = True
                        self.keyswitch['K_r'] = True
                self.reloaddelay = 0
            else:
                self.keyswitch['K_r'] = False

        else:
            self.reloaddelay += dtime
            if self.reloaddelay >= self.reloadtime * dtime * TARGET_FPS:
                self.reloaddelay = 0
                if aviableammunition := functions.founditems(owner.inventory.inventoryslots, self.ammunition):
                    for key, value in aviableammunition.items():
                        aviable = aviableammunition[key].amount
                        aviableammunition[key].amount -= 1
                        self.ammo += 1
                        if (self.ammo == self.maxammo) or not aviableammunition:
                            self.reloading = False
                            break   
                else:
                    self.reloading = False
