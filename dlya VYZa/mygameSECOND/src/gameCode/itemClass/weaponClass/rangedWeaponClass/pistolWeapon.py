from gameCode import functions
from . import defaultRangedWeapon

class Pistol(defaultRangedWeapon.RangedWeapon):

    def __init__(self, itemName, itemTextureLink, itemIconLink, spreadingAngleValue, shotingRangeValue, shotingSpeedValue, reloadingTimeValue, pickingTimeValue, damageAmountValue, bulletAmountValue, ammoAmountValue, maxAmmoAmountValue, ammunitionType):
        super().__init__(itemName, itemTextureLink, itemIconLink, spreadingAngleValue, shotingRangeValue, shotingSpeedValue, reloadingTimeValue, pickingTimeValue, damageAmountValue, bulletAmountValue, ammoAmountValue, maxAmmoAmountValue, ammunitionType)
        self.secondItemType = 'pistol'

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

    def useMake(self, entity, mouse):
        if self.using and (not self.used) and (not self.usingDelayValue):
            self.ammunitionValue.useMake(entity=entity, targets=entity.enemyGroup, mouse=mouse, spreadingAngleValue=self.spreadingAngleValue, shotingSpeedValue=self.shotingSpeedValue, damageAmountValue=self.damageAmountValue, ammoAmountValue=self.ammoAmountValue)
            self.ammoAmountValue -= 1
            self.used = True
