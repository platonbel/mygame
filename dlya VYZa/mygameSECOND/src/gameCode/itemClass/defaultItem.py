import pygame

class Item():
    
    def __init__(self, itemName=None, itemTextureLink=None, itemIconLink=None):

        self.itemName = itemName
        self.itemIconLink = itemIconLink if itemIconLink else "src/assets/textures/default_icon.png"
        self.itemTextureLink = itemTextureLink
        self.firstItemType = 'default'
        self.secondItemType = 'default'

        self.amountValue = 1

        self.pickingTimeValue = 0
        self.usingTimeValue = 0
        self.reloadingTimeValue = 0

        self.pickingDelayValue = 0
        self.usingDelayValue = 0
        self.reloadingDelayValue = 0

        self.pickingState = False
        self.usingState = False
        self.reloadingState = False

        self.pickedState = False
        self.usedState = False
        self.reloadedState = False

        self.stackableState = True
        self.existState = True

        self.keySwitch = {}
        self.mouseSwitch = {}

    def existChesk(self):
        if self.amountValue <= 0:
            self.__del__()

    def pickingUpdate(self, dtime):
        if not self.pickedState:
            if self.picking:
                self.pickingDelayValue += dtime
            else:
                self.pickingDelayValue = 0
        self.pickMake()
    
    def pickMake(self):
        if self.pickingDelayValue >= self.pickingTimeValue:
            self.pickingDelayValue = 0
            self.pickingState = False
            self.pickedState = True

    def update(self, entity=None, mouse=None, mouseState=None, keyState=None, dtime=None, TARGET_FPS=None):
        self.existChesk()
        if self.pickedState:
            pass
        else:
            self.pickingUpdate(dtime)

    def __del__(self):
        self.existState = False



