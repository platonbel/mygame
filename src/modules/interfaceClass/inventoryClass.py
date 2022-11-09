import pygame
from modules import interfaceClass, shapeClass, textClass

class Inventory():

    def __init__(self, screen):
        self.hided = True
        self.inventorySlotsBackground_image = shapeClass.privateShape.Shape(image="src/assets/textures/inventory_slots_background.png", position=(22, screen.get_height()-22), side='bottomleft', layer=0, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.inventorySlots_image = shapeClass.privateShape.Shape(image="src/assets/textures/inventory_slots.png", position=(30, screen.get_height()-166), side='bottomleft', layer=1, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.inventoryslots = {

            '1': (shapeClass.privateShape.Shape(position=(82, screen.get_height()-218), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer),
            textClass.privateText.Text(position=(114, screen.get_height()-186), side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)), 

            '2': (shapeClass.privateShape.Shape(position=(186, screen.get_height()-218), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer),
            textClass.privateText.Text(position=(218, screen.get_height()-186), side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),

            '3': (shapeClass.privateShape.Shape(position=(290, screen.get_height()-218), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(position=(332, screen.get_height()-186), side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '4': (shapeClass.privateShape.Shape(position=(394, screen.get_height()-218), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(position=(426, screen.get_height()-186), side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '5': (shapeClass.privateShape.Shape(position=(498, screen.get_height()-218), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(position=(530, screen.get_height()-186), side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '6': (shapeClass.privateShape.Shape(position=(82, screen.get_height()-322), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(position=(114, screen.get_height()-290), side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '7': (shapeClass.privateShape.Shape(position=(186, screen.get_height()-322), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(position=(218, screen.get_height()-290), side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '8': (shapeClass.privateShape.Shape(position=(290, screen.get_height()-322), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(position=(322, screen.get_height()-290), side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '9': (shapeClass.privateShape.Shape(position=(394, screen.get_height()-322),side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(position=(426, screen.get_height()-290), side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '10': (shapeClass.privateShape.Shape(position=(498, screen.get_height()-322), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(position=(530, screen.get_height()-290), side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '11': (shapeClass.privateShape.Shape(position=(82, screen.get_height()-426), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(position=(114, screen.get_height()-394), side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '12': (shapeClass.privateShape.Shape(position=(186, screen.get_height()-426), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(position=(218, screen.get_height()-394), side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '13': (shapeClass.privateShape.Shape(position=(290, screen.get_height()-426), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(position=(322, screen.get_height()-394), side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '14': (shapeClass.privateShape.Shape(position=(394, screen.get_height()-426), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(position=(426, screen.get_height()-394), side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '15': (shapeClass.privateShape.Shape(position=(498, screen.get_height()-426), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer),
            textClass.privateText.Text(position=(530, screen.get_height()-394), side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer))
        }
    def inventoryRender(self, player):
        if player:
            if player.inventory.opened:
                for key, value in player.inventory.inventoryslots.items():
                    if value:
                        self.inventoryslots[key][0].imageedit(value.itemicon)
                        if value.itemtype == 'ammunition':
                            self.inventoryslots[key][1].textedit(str(value.amount), (0, 0, 0))
                    else:
                        self.inventoryslots[key][0].imageedit("src/assets/textures/empty_icon.png")
                        self.inventoryslots[key][1].textedit(None, (0, 0, 0))
                self.hided = False
            else:
                self.hided = True
        else:
            self.hided = True

        self.inventorySlotsBackground_image.hided = self.hided
        self.inventorySlots_image.hided = self.hided
        for key, value in self.inventoryslots.items():
            self.inventoryslots[key][0].hided = self.hided
            self.inventoryslots[key][1].hided = self.hided