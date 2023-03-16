import pygame

from gameCode.itemClass import defaultItem

class Supplies(defaultItem.Item):
    
    def __init__(self, itemName, itemTextureLink, itemIconLink, secondItemType='default', effectsGroup=dict(), usingTimeValue=0, pickingTimeValue=0):
        super().__init__(itemName, itemTextureLink, itemIconLink)

        self.firstItemType = 'supplies'
        self.secondItemType = secondItemType
        self.effectsGroup = effectsGroup

        self.usingTimeValue = usingTimeValue
        self.pickingTimeValue = pickingTimeValue

        self.stackable = True

        self.keySwitch = {'K_e': False}

    def usingUpdate(self, entity, keyState, dtime, TARGET_FPS):
        if keyState[pygame.K_e]:
            if (not self.keySwitch['K_e']):
                self.using = True
                self.keySwitch['K_e'] = True
        else:
            self.keySwitch['K_e'] = False

        if self.using:
            self.usingDelayValue = (self.usingDelayValue + dtime)
            if self.usingDelayValue >= dtime * TARGET_FPS * self.usingTimeValue: 
                self.usingDelayValue = 0
                self.used = True
        else:
            self.usingDelayValue = 0

        self.useMake(entity)

    def useMake(self, entity):
        if self.used:
            for key, effect in self.effectsGroup.items():
                entity.effects.effectsGroup[key].setStats(effect.value, effect.time)
            self.amountValue -= 1
            self.used = True

    def update(self, entity=None, mouse=None, mouseState=None, keyState=None, dtime=None, TARGET_FPS=None):
        self.existChesk()
        if self.picked:
            self.usingUpdate(entity, keyState, dtime, TARGET_FPS)
        else:
            self.pickingUpdate(dtime)

        
