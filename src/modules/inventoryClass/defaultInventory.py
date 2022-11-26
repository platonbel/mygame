import pygame

class Inventory():
    
    def __init__(self):
        self.opened = False

        self.inventoryslots = {
            '1': None, '2': None, '3': None, '4': None, '5': None, 
            '6': None, '7': None, '8': None, '9': None, '10': None, 
            '11': None, '12': None, '13': None, '14': None, '15': None,
            '16': None, '17': None, '18': None, '19': None, '20': None,
        }
    
        self.currentslot = None
        
        self.currenttempslot = None

        self.tempitem = None
        self.item = None

        self.keyswith = {'K_TAB': False, 'K_0': False, 'K_1': False, 'K_2': False, 'K_3': False, 'K_4': False, 'K_5': False}
    
    def inventoryRender(self, keystate):
        #open inventory
        if keystate[pygame.K_TAB]:
            if not self.keyswith['K_TAB']:
                self.opened = not self.opened
            self.keyswith['K_TAB'] = True
        else:
            self.keyswith['K_TAB'] = False
        #inventory slots updating
        for key, value in self.inventoryslots.items():
            if value:
                value.existChesk()
                if not value.exist:
                    self.inventoryslots[key] = None
        #tempitem slot updating
        if self.tempitem:
            self.tempitem.existChesk()
            if not self.tempitem.exist:
                self.tempitem = None
                
    def quickAccesBarRender(self, owner, mouse, mousestate, keystate, dtime, TARGET_FPS):
        #binding to choosed slot the current key of slot
        if keystate[pygame.K_1]:
            if not self.keyswith['K_1']:
                if self.currentslot != '1':
                    self.currentslot = '1'
                else:
                    self.currentslot = None
                if self.item:
                    self.item.picked = False
                    self.item.pickingdelay = 0
            self.keyswith['K_1'] = True
        else:
            self.keyswith['K_1'] = False
        
        if keystate[pygame.K_2]:
            if not self.keyswith['K_2']:
                if self.currentslot != '2':
                    self.currentslot = '2'
                    self.item = self.inventoryslots[self.currentslot]
                else:
                    self.currentslot = None
                    self.item = None
                if self.item:
                    self.item.picked = False
                    self.item.pickingdelay = 0
            self.keyswith['K_2'] = True
        else:
            self.keyswith['K_2'] = False

        if keystate[pygame.K_3]:
            if not self.keyswith['K_3']:
                if self.currentslot != '3':
                    self.currentslot = '3'
                    self.item = self.inventoryslots[self.currentslot]
                else:
                    self.currentslot = None
                    self.item = None
                if self.item:
                    self.item.picked = False
                    self.item.pickingdelay = 0
            self.keyswith['K_3'] = True
        else:
            self.keyswith['K_3'] = False

        if keystate[pygame.K_4]:
            if not self.keyswith['K_4']:
                if self.currentslot != '4':
                    self.currentslot = '4'
                    self.item = self.inventoryslots[self.currentslot]
                else:
                    self.currentslot = None
                    self.item = None
                if self.item:
                    self.item.picked = False
                    self.item.pickingdelay = 0
            self.keyswith['K_4'] = True
        else:
            self.keyswith['K_4'] = False

        if keystate[pygame.K_5]:
            if not self.keyswith['K_5']:
                if self.currentslot != '5':
                    self.currentslot = '5'
                    self.item = self.inventoryslots[self.currentslot]
                else:
                    self.currentslot = None
                    self.item = None
                if self.item:
                    self.item.picked = False
                    self.item.pickingdelay = 0
            self.keyswith['K_5'] = True
        else:
            self.keyswith['K_5'] = False
        #checking for choosing item in current slot
        if self.item != (self.inventoryslots[self.currentslot] if self.currentslot else None):
            self.item = (self.inventoryslots[self.currentslot] if self.currentslot else None)
            if self.item:
                self.item.picked = False
                self.item.pickingdelay = 0
        #None-slot
        if not self.currentslot:
            self.item = None

        self.choosedItemUpdate(owner, mouse, mousestate, keystate, dtime, TARGET_FPS)

    def choosedItemUpdate(self, owner, mouse, mousestate, keystate, dtime, TARGET_FPS):
        #presets before full picking item
        if self.item:
            if not self.item.picked:
                self.item.picking(dtime)
            else:
                match self.item.itemtype:
                    case 'rangedWeapon':
                        self.item.update(owner, mouse, mousestate, keystate, dtime, TARGET_FPS)
                    case 'ammunition':
                        self.item.update()
                    case 'supplies':
                        self.item.update(owner, keystate, dtime, TARGET_FPS)




        
        