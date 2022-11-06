import pygame
from modules import interfaceClass, shapeClass

class Inventory():

    def __init__(self, screen):
        self.hided = True
        self.inventorySlotsBackground = shapeClass.privateShape.Shape(image="src/assets/textures/inventory_slots_background.png", position=(22, screen.get_height()-22), side='bottomleft', layer=0, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.inventorySlots = shapeClass.privateShape.Shape(image="src/assets/textures/inventory_slots.png", position=(30, screen.get_height()-166), side='bottomleft', layer=1, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)

    def inventoryRender(self, player):
        if player:
            if player.inventoryc.opened:
                #for item in player.inventory.inventoryslots:
                self.hided = False
            else:
                self.hided = True
        else:
            self.hided = True

        self.inventorySlotsBackground.hided = self.hided
        self.inventorySlots.hided = self.hided