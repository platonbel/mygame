import pygame
import math
import copy
from modules import functions
from modules.itemClass.instances import ammunitionGroup
from modules.itemClass.weaponClass import defaultWeapon

class RangedWeapon(defaultWeapon.Weapon):
    
    def __init__(self, itemname, iconimage=None, spreadangle=0, shotrange=0, shotspeed=0, reloadtime=0, pickingtime=0, damage=0, bulletamount=1, ammo=math.inf, maxammo=math.inf, ammunitiontype='default'):
        super().__init__(itemname, iconimage, pickingtime)

        self.spreadangle = spreadangle
        self.shotrange = shotrange
        self.shotspeed = shotspeed
        self.reloadtime = reloadtime
        self.damage = damage
        self.bulletamount = bulletamount

        self.shotdelay = 0 
        self.reloaddelay = 0

        self.itemtype = 'rangedWeapon'
        self.weapontype = 'default'
        self.ammunitiontype = ammunitiontype

        self.ammo = ammo
        self.maxammo = maxammo
        self.ammunition = copy.deepcopy(ammunitionGroup.items[self.ammunitiontype])

        self.stackable = False
        self.shooting = False
        self.reloading = False

        self.keyswitch = {'K_r': False}
        self.mouseswitch = {'0': False}

    def picking(self, dtime):
        if not self.picked:
            self.pickingdelay += dtime
            if self.pickingdelay >= self.pickingtime:
                self.pickingdelay = 0
                self.shooting = False
                self.reloading = False
                self.picked = True

    def attack(self, owner, mouse, mousestate, dtime, TARGET_FPS):
        if mousestate[0]:
            if not self.mouseswitch['0']:    
                if self.ammo:
                    self.ammunition.use(owner=owner, targets=owner.enemygroup, mouse=mouse, spreadangle=self.spreadangle, shotrange=self.shotrange, damage=self.damage, bulletamount=self.bulletamount)
                    self.ammo -= 1
                    self.shooting = True
                    self.mouseswitch['0'] = True
        else:
            self.shooting = False
            self.mouseswitch['0'] = False
            
        
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
                    for key in aviableammunition.keys():
                        aviable = aviableammunition[key].amount
                        aviableammunition[key].amount -= min(aviable, self.maxammo-self.ammo)
                        self.ammo += min(aviable, self.maxammo-self.ammo)
                        if (self.ammo == self.maxammo) or not aviableammunition:
                            break
                self.reloading = False

    def update(self, owner, mouse, mousestate, keystate, dtime, TARGET_FPS):
        self.existChesk()
        if self.picked:
            self.reload(owner, keystate, dtime, TARGET_FPS)
            self.attack(owner, mouse, mousestate, dtime, TARGET_FPS)

        
