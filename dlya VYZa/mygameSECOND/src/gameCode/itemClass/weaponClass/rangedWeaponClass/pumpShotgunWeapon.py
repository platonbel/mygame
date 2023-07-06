import pygame

from gameCode import functions
from . import defaultRangedWeapon

class PumpShotgun(defaultRangedWeapon.RangedWeapon):

    def __init__(self, itemName, itemTextureLink, itemIconLink, spreadingAngleValue, shotingRangeValue, shotingSpeedValue, reloadingTimeValue, pickingTimeValue, damageAmountValue, bulletAmountValue, ammoAmountValue, maxAmmoAmountValue, ammunitionType):
        super().__init__(itemName, itemTextureLink, itemIconLink, spreadingAngleValue, shotingRangeValue, shotingSpeedValue, reloadingTimeValue, pickingTimeValue, damageAmountValue, bulletAmountValue, ammoAmountValue, maxAmmoAmountValue, ammunitionType)
        self.secondItemType = 'pumpShotgun'
        
    def reloadingUpdate(self, entity, keyState, dtime, TARGET_FPS):
        if keyState[pygame.K_r]:
            if (not self.keySwitch['K_r']) and (not self.reloaded) and (not self.reloading):
                self.reloading = True
                self.keySwitch['K_r'] = True
        else:
            self.keySwitch['K_r'] = False

        if self.reloading:
            self.reloadingDelayValue = self.reloadingDelayValue+dtime if not self.reloadingDelayValue else dtime
            if self.reloadingDelayValue >= self.reloadingTimeValue * dtime * TARGET_FPS:
                self.reloadingDelayValue = 0
                self.reloading = False
                self.reloaded = True
        self.reloadMake(entity)

    def usingUpdate(self, entity, mouse, mouseState, dtime, TARGET_FPS):
        if mouseState[0]:
            if (not self.mouseSwitch['0']) and self.ammoAmountValue:
                self.using = True
                self.mouseSwitch['0'] = True
            else:
                self.using = False
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

    def reloadMake(self, entity):
        if self.reloaded:
            if aviableAmmunition := functions.founditems(entity.inventory.inventoryslots, self.ammunitionValue):
                for key in aviableAmmunition.keys():
                    aviableAmmunition[key].amountValue -= 1
                    self.ammoAmountValue += 1
                    if (self.ammoAmountValue == self.maxAmmoAmountValue) or (not aviableAmmunition):
                        break
            self.reloaded = False

    def useMake(self, entity, mouse):
        if self.using and (not self.used) and (not self.usingDelayValue):
            self.ammunitionValue.useMake(entity=entity, targets=entity.enemyGroup, mouse=mouse, spreadingAngleValue=self.spreadingAngleValue, shotingSpeedValue=self.shotingSpeedValue, damageAmountValue=self.damageAmountValue, ammoAmountValue=self.ammoAmountValue)
            self.ammoAmountValue -= 1
            self.used = True