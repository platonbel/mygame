import pygame

class Inventory():
    
    def __init__(self):
        self.opened = False

        self.inventoryslots = {
            None: None,
            '1': None, '2': None, '3': None, '4': None, '5': None, 
            '6': None, '7': None, '8': None, '9': None, '10': None, 
            '11': None, '12': None, '13': None, '14': None, '15': None,
            '16': None, '17': None, '18': None, '19': None, '20': None,
        }
        self.tempitemslot = None

    
        self.prevslot = None
        self.currentslot = None
        self.currentitem = self.inventoryslots[self.currentslot]

        self.keyswith = {'K_TAB': False, 'K_0': False, 'K_1': False, 'K_2': False, 'K_3': False, 'K_4': False, 'K_5': False}
    
    def inventoryRender(self, keystate):
        if keystate[pygame.K_TAB]:
            if not self.keyswith['K_TAB']:
                self.opened = not self.opened
            self.keyswith['K_TAB'] = True
        else:
            self.keyswith['K_TAB'] = False
        for key, value in self.inventoryslots.items():
            if value:
                if value.exist:
                    value.existChesk()
                else:
                    self.inventoryslots[key] = None

    def quickAccesBarRender(self, keystate, dtime, owner):
        if keystate[pygame.K_1]:
            if not self.keyswith['K_1']:
                if self.currentitem:
                    self.currentitem.picked = False
                if self.currentslot != '1':
                    self.currentslot = '1'
                else:
                    self.currentslot = None
                self.currentitem = self.inventoryslots[self.currentslot]
            self.keyswith['K_1'] = True
        else:
            self.keyswith['K_1'] = False
        
        if keystate[pygame.K_2]:
            if not self.keyswith['K_2']:
                if self.currentitem:
                    self.currentitem.picked = False
                if self.currentslot != '2':
                    self.currentslot = '2'
                else:
                    self.currentslot = None
                self.currentitem = self.inventoryslots[self.currentslot]
            self.keyswith['K_2'] = True
        else:
            self.keyswith['K_2'] = False

        if keystate[pygame.K_3]:
            if not self.keyswith['K_3']:
                if self.currentitem:
                    self.currentitem.picked = False
                if self.currentslot != '3':
                    self.currentslot = '3'
                else:
                    self.currentslot = None
                self.currentitem = self.inventoryslots[self.currentslot]
            self.keyswith['K_3'] = True
        else:
            self.keyswith['K_3'] = False

        if keystate[pygame.K_4]:
            if not self.keyswith['K_4']:
                if self.currentitem:
                    self.currentitem.picked = False
                if self.currentslot != '4':
                    self.currentslot = '4'
                else:
                    self.currentslot = None
                self.currentitem = self.inventoryslots[self.currentslot]
            self.keyswith['K_4'] = True
        else:
            self.keyswith['K_4'] = False

        if keystate[pygame.K_5]:
            if not self.keyswith['K_5']:
                if self.currentitem:
                    self.currentitem.picked = False
                if self.currentslot != '5':
                    self.currentslot = '5'
                else:
                    self.currentslot = None
                self.currentitem = self.inventoryslots[self.currentslot]
            self.keyswith['K_5'] = True
        else:
            self.keyswith['K_5'] = False

        self.choosedItemUpdate(dtime, owner)

        if self.currentitem != self.inventoryslots[self.currentslot]:
            self.currentitem = self.inventoryslots[self.currentslot]
            if self.currentitem:
                self.currentitem.picked = False

    def choosedItemUpdate(self, dtime, owner):
        if self.currentitem != None:
            if self.currentitem.itemtype == 'rangedWeapon' and not self.currentitem.picked:
                self.currentitem.picking(dtime)
                self.currentitem.shooting = False
                self.currentitem.reloading = False
                self.currentitem.owner = owner
                self.currentitem.targets = self.currentitem.owner.enemygroup

    def founditem(self, item, foundkey):
        for key, value in self.inventoryslots.items():
            if value:
                match foundkey:
                    case 'ammunitiontype':
                        if value.itemtype == 'ammunition':
                            if value.ammunitiontype == item:
                                return key, value
        else:
            return None, None
        
        