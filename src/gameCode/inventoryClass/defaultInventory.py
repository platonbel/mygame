import pygame

class Inventory():
    
    def __init__(self):

        self.inventorySlots = {
            '1': None, '2': None, '3': None, '4': None, '5': None, 
            '6': None, '7': None, '8': None, '9': None, '10': None, 
            '11': None, '12': None, '13': None, '14': None, '15': None,
            '16': None, '17': None, '18': None, '19': None, '20': None,
        }
    
        self.currentSlot = None
        
        self.currentTempSlot = None

        self.tempItem = None
        self.item = None

        self.opened = False

        self.keySwith = {'K_TAB': False, 'K_0': False, 'K_1': False, 'K_2': False, 'K_3': False, 'K_4': False, 'K_5': False}
    
    def inventoryRender(self, keyState):
        #open inventory
        if keyState[pygame.K_TAB]:
            if not self.keySwith['K_TAB']:
                self.opened = not self.opened
                self.keySwith['K_TAB'] = True
        else:
            self.keySwith['K_TAB'] = False
        #inventory slots updating
        for key, value in self.inventorySlots.items():
            if value:
                value.existCheck()
                if not value.exist:
                    self.inventorySlots[key] = None
        #tempitem slot updating
        if self.tempItem:
            self.tempItem.existChesk()
            if not self.tempItem.exist:
                self.tempItem = None
                
    def quickAccesBarRender(self, keyState):
        #binding to choosed slot the current key of slot
        if keyState[pygame.K_1]:
            if not self.keySwith['K_1']:
                if self.currentSlot != '1':
                    self.currentSlot = '1'
                else:
                    self.currentSlot = None
                self.keySwith['K_1'] = True
        else:
            self.keySwith['K_1'] = False
        
        if keyState[pygame.K_2]:
            if not self.keySwith['K_2']:
                if self.currentSlot != '2':
                    self.currentSlot = '2'      
                else:
                    self.currentSlot = None
                self.keySwith['K_2'] = True
        else:
            self.keySwith['K_2'] = False

        if keyState[pygame.K_3]:
            if not self.keySwith['K_3']:
                if self.currentSlot != '3':
                    self.currentSlot = '3'
                else:
                    self.currentSlot = None
                self.keySwith['K_3'] = True
        else:
            self.keySwith['K_3'] = False

        if keyState[pygame.K_4]:
            if not self.keySwith['K_4']:
                if self.currentSlot != '4':
                    self.currentSlot = '4'
                else:
                    self.currentSlot = None
                self.keySwith['K_4'] = True
        else:
            self.keySwith['K_4'] = False

        if keyState[pygame.K_5]:
            if not self.keySwith['K_5']:
                if self.currentSlot != '5':
                    self.currentSlot = '5'
                else:
                    self.currentSlot = None
                self.keySwith['K_5'] = True
        else:
            self.keySwith['K_5'] = False
        
        #checking for choosing item in current slot
        if self.item != (self.inventorySlots[self.currentSlot] if self.currentSlot else None):
            self.item = (self.inventorySlots[self.currentSlot] if self.currentSlot else None)
            if self.item:
                self.item.picked = False

    def choosedItemUpdate(self, owner, mouse, mouseState, keyState, dtime, TARGET_FPS):
        if self.item:
            if self.item.picked:
                self.item.update(owner, mouse, mouseState, keyState, dtime, TARGET_FPS)
            else:
                self.item.picking = True


        
        