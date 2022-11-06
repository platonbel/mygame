import pygame

class Inventory():
    
    def __init__(self):
        self.opened = False

        self.inventoryslots = {
            '1': None, '2': None, '3': None, '4': None, '5': None, 
            '6': None, '7': None, '8': None, '9': None, '10': None, 
            '11': None, '12': None, '13': None, '14': None, '15': None
        }
        self.keyswith = {'K_TAB': False}
    
    def inventoryRender(self, keystate, owner):
        if keystate[pygame.K_TAB]:
            if not self.keyswith['K_TAB']:
                self.opened = not self.opened
            self.keyswith['K_TAB'] = True
        else:
            self.keyswith['K_TAB'] = False
        