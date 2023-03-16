import pygame

import math
from gameCode import functions
from gameCode.itemClass.instances import ammunitionGroup
from gameCode.itemClass import defaultItem

class RangedWeapon(defaultItem.Item):
    
    def __init__(self, itemName=None, itemTextureLink=None, itemIconLink=None, spreadingAngleValue=0, shotingRangeValue=0, shotingSpeedValue=0, reloadingTimeValue=0, pickingTimeValue=0, damageAmountValue=0, bulletAmountValue=1, ammoAmountValue=math.inf, maxAmmoAmountValue=math.inf, ammunitionType='default'):
        super().__init__(itemName, itemTextureLink, itemIconLink)

        self.firstItemType = 'rangedWeapon'
        self.secondItemType = 'default'
        self.ammunitionType = ammunitionType

        self.pickingTimeValue = pickingTimeValue
        self.reloadingTimeValue = reloadingTimeValue

        self.spreadingAngleValue = spreadingAngleValue
        self.shotingRangeValue = shotingRangeValue
        self.shotingSpeedValue = shotingSpeedValue
        self.damageAmountValue = damageAmountValue
        self.bulletAmountValue = bulletAmountValue

        self.ammoAmountValue = ammoAmountValue
        self.maxAmmoAmountValue = maxAmmoAmountValue
        self.ammunitionValue = functions.createItem(ammunitionGroup.items[self.ammunitionType])

        self.stackable = False
        self.keySwitch = {'K_r': False}
        self.mouseSwitch = {'0': False}

    def pickingUpdate(self, dtime):
        if not self.picked:
            if self.picking:
                self.pickingDelayValue += dtime
            else:
                self.pickingDelayValue = 0
        self.pickMake()

    def usingUpdate(self, entity, mouse, mouseState, dtime, TARGET_FPS):
        if mouseState[0]:
            if (not self.mouseSwitch['0']) and self.ammoAmountValue:
                self.using = True
                self.mouseSwitch['0'] = True
            else:
                pass
        else:
            self.using = False
            self.mouseSwitch['0'] = False

        if self.used:
            self.usingDelayValue = (self.usingDelayValue + dtime*self.shotingSpeedValue)
            if self.usingDelayValue >= TARGET_FPS: 
                self.usingDelayValue = 0
                self.used = False
        else:
            self.usingDelayValue = 0

        self.useMake(entity, mouse)

    def reloadingUpdate(self, entity, keyState, dtime, TARGET_FPS):
        if keyState[pygame.K_r]:
            if (not self.keySwitch['K_r']) and (not self.reloaded) and (not self.reloading):
                self.reloading = True
                self.keySwitch['K_r'] = True
        else:
            self.keySwitch['K_r'] = False

        if self.reloading:
            self.reloadingDelayValue = (self.reloadingDelayValue + dtime)
            if self.reloadingDelayValue >= self.reloadingTimeValue * dtime * TARGET_FPS:
                self.reloadingDelayValue = 0
                self.reloading = False
                self.reloaded = True
        else:
            self.reloadingDelayValue = 0
        self.reloadMake(entity)

    def pickMake(self):
        if self.pickingDelayValue >= self.pickingTimeValue:
            self.pickingDelayValue = 0
            self.picking = False
            self.picked = True
            self.used = False
            self.reloaded = False

    def reloadMake(self, entity):
        if self.reloaded:
            if aviableAmmunition := functions.founditems(entity.inventory.inventoryslots, self.ammunitionValue):
                for key in aviableAmmunition.keys():
                    aviableAmmunition[key].amountValue -= min(aviableAmmunition[key].amountValue, self.maxAmmoAmountValue-self.ammoAmountValue)
                    self.ammoAmountValue += min(aviableAmmunition[key].amountValue, self.maxAmmoAmountValue-self.ammoAmountValue)
                    if (self.ammoAmountValue == self.maxAmmoAmountValue) or (not aviableAmmunition):
                        break
            self.reloaded = False

    def useMake(self, entity, mouse):
        if self.using and (not self.used) and (not self.usingDelayValue):
            self.ammunitionValue.useMake(entity=entity, targets=entity.enemyGroup, mouse=mouse, spreadingAngleValue=self.spreadingAngleValue, shotingSpeedValue=self.shotingSpeedValue, damageAmountValue=self.damageAmountValue, ammoAmountValue=self.ammoAmountValue)
            self.ammoAmountValue -= 1
            self.used = True

    def update(self, entity, mouse, mouseState, keyState, dtime, TARGET_FPS):
        self.existChesk()
        if self.picked:
            self.reloadingUpdate(entity, keyState, dtime, TARGET_FPS)
            self.usingUpdate(entity, mouse, mouseState, dtime, TARGET_FPS)
        else:
            self.pickingUpdate(dtime)

        
