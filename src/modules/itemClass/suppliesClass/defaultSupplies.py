import pygame

from modules.itemClass import defaultItem

class Supplies(defaultItem.Item):
    
    def __init__(self, itemname, iconimage, suppliestype='default', instanthealthheal=0, instantstaminaheal=0, healthregeneration=0, healthregenerationtime=0, staminaregeneration=0, staminaregenerationtime=0, speedup=0, speeduptime=0, usingtime=0, pickingtime=0):
        super().__init__(itemname, iconimage, pickingtime)

        self.itemtype = 'supplies'
        self.suppliestype = suppliestype

        self.instanthealthheal = instanthealthheal
        self.instantstaminaheal = instantstaminaheal
        
        self.healthregeneration = healthregeneration
        self.healthregenerationtime = healthregenerationtime

        self.staminaregeneration = staminaregeneration
        self.staminaregenerationtime = staminaregenerationtime

        self.speedup = speedup
        self.speeduptime = speeduptime

        self.usingtime = usingtime
        self.usingdelay = 0
        
        self.stackable = True
        self.using = False

        self.keyswitch = {'K_e': False}

    def picking(self, dtime):
        if not self.picked:
            self.pickingdelay += dtime
            if self.pickingdelay >= self.pickingtime:
                self.pickingdelay = 0
                self.using = False
                self.picked = True

    def use(self, owner, keystate, dtime, TARGET_FPS):
        if not self.using:
            if keystate[pygame.K_e]:
                if not self.keyswitch['K_e']:
                    self.using = True
                    self.keyswitch['K_e'] = True
            else:
                self.keyswitch['K_e'] = False
        else:
            self.usingdelay += dtime
            if self.usingdelay >= self.usingtime * dtime * TARGET_FPS:
                self.usingdelay = 0
                self.amount -= 1

                if self.instanthealthheal:
                    owner.effects.instanthealthheal = self.instanthealthheal
                if self.instantstaminaheal:
                    owner.effects.instantstaminaheal = self.instantstaminaheal

                if owner.effects.healthregeneration * owner.effects.healthregenerationtime < self.healthregeneration * self.healthregenerationtime:
                    owner.effects.healthregeneration = self.healthregeneration
                    owner.effects.healthregenerationtime = self.healthregenerationtime

                if owner.effects.staminaregeneration * owner.effects.staminaregenerationtime < self.staminaregeneration * self.staminaregenerationtime:
                    owner.effects.staminaregeneration = self.staminaregeneration
                    owner.effects.staminaregenerationtime = self.staminaregenerationtime

                if owner.effects.speedup * owner.effects.speeduptime < self.speedup * self.speeduptime:
                    owner.effects.speedup = self.speedup
                    owner.effects.speeduptime = self.speeduptime

                self.using = False

    def update(self, owner, keystate, dtime, TARGET_FPS):
        self.existChesk()
        if self.picked:
            self.use(owner, keystate, dtime, TARGET_FPS)

        
