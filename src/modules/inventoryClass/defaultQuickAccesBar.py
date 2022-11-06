import pygame
from modules import interfaceClass

class QuickAccesBar():

    def __init__(self):
        self.prevslot = None
        self.currentslot = None
        self.barslots = {None: None, '1': None, '2': None, '3': None, '4': None, '5': None}
        self.currentitem = self.barslots[self.currentslot]
        self.keyswith = {'K_0': False, 'K_1': False, 'K_2': False, 'K_3': False, 'K_4': False, 'K_5': False}

    def quickAccesBarRender(self, keystate, owner):
        if keystate[pygame.K_1]:
            if not self.keyswith['K_1']:
                if self.currentslot != '1':
                    self.currentslot = '1'
                else:
                    self.currentslot = None
                self.currentitem = self.barslots[self.currentslot]
                self.choosedItemUpdate(owner)
            self.keyswith['K_1'] = True
        else:
            self.keyswith['K_1'] = False
        
        if keystate[pygame.K_2]:
            if not self.keyswith['K_2']:
                if self.currentslot != '2':
                    self.currentslot = '2'
                else:
                    self.currentslot = None
                self.currentitem = self.barslots[self.currentslot]
                self.choosedItemUpdate(owner)
            self.keyswith['K_2'] = True
        else:
            self.keyswith['K_2'] = False

        if keystate[pygame.K_3]:
            if not self.keyswith['K_3']:
                if self.currentslot != '3':
                    self.currentslot = '3'
                else:
                    self.currentslot = None
                self.currentitem = self.barslots[self.currentslot]
                self.choosedItemUpdate(owner)
            self.keyswith['K_3'] = True
        else:
            self.keyswith['K_3'] = False

        if keystate[pygame.K_4]:
            if not self.keyswith['K_4']:
                if self.currentslot != '4':
                    self.currentslot = '4'
                else:
                    self.currentslot = None
                self.currentitem = self.barslots[self.currentslot]
                self.choosedItemUpdate(owner)
            self.keyswith['K_4'] = True
        else:
            self.keyswith['K_4'] = False

        if keystate[pygame.K_5]:    
            if not self.keyswith['K_5']:
                if self.currentslot != '5':
                    self.currentslot = '5'
                else:
                    self.currentslot = None
                self.currentitem = self.barslots[self.currentslot]
                self.choosedItemUpdate(owner)
            self.keyswith['K_5'] = True
        else:
            self.keyswith['K_5'] = False
    
    def choosedItemUpdate(self, owner):
        if self.currentitem != None:
            if self.currentitem.itemtype == 'rangedWeapon' and not self.currentitem.picked:
                self.currentitem.shooting = False
                self.currentitem.reloading = False
                self.currentitem.picked = False
                self.currentitem.owner = owner
                self.currentitem.targets = self.currentitem.owner.enemygroup
                self.currentitem.ammunition = self.currentitem.owner.inventory[self.currentitem.ammunitiontype]
                self.currentitem.targets = self.currentitem.owner.enemygroup
