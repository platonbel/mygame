import pygame
from modules import interfaceClass, shapeClass, textClass

class Inventory():

    def __init__(self, screen):
        self.inventoryhided = True
        self.quickaccesbarhided = True

        self.inventorySlotsBackground_image = shapeClass.privateShape.Shape(image="src/assets/textures/inventory_slots_background.png", position=(22, screen.get_height()-22), side='bottomleft', layer=0, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.inventorySlots_image = shapeClass.privateShape.Shape(image="src/assets/textures/inventory_slots.png", position=(30, screen.get_height()-166), side='bottomleft', layer=1, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.quickAccesBar = shapeClass.privateShape.Shape(image="src/assets/textures/quick_acces_bar_0.png", position=(30, screen.get_height()-30), side='bottomleft', layer=1, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)

        self.inventoryslots = {

            '1': interfaceClass.defaultIcon.Icon(position=(82, screen.get_height()-82)),
            '2': interfaceClass.defaultIcon.Icon(position=(186, screen.get_height()-82)),
            '3': interfaceClass.defaultIcon.Icon(position=(290, screen.get_height()-82)),
            '4': interfaceClass.defaultIcon.Icon(position=(394, screen.get_height()-82)),
            '5': interfaceClass.defaultIcon.Icon(position=(498, screen.get_height()-82)),
            '6': interfaceClass.defaultIcon.Icon(position=(82, screen.get_height()-426)),
            '7': interfaceClass.defaultIcon.Icon(position=(186, screen.get_height()-426)),
            '8': interfaceClass.defaultIcon.Icon(position=(290, screen.get_height()-426)),
            '9': interfaceClass.defaultIcon.Icon(position=(394, screen.get_height()-426)),
            '10': interfaceClass.defaultIcon.Icon(position=(498, screen.get_height()-426)),
            '11': interfaceClass.defaultIcon.Icon(position=(82, screen.get_height()-322)),
            '12': interfaceClass.defaultIcon.Icon(position=(186, screen.get_height()-322)),
            '13': interfaceClass.defaultIcon.Icon(position=(290, screen.get_height()-322)),
            '14': interfaceClass.defaultIcon.Icon(position=(394, screen.get_height()-322)),
            '15': interfaceClass.defaultIcon.Icon(position=(498, screen.get_height()-322)),
            '16': interfaceClass.defaultIcon.Icon(position=(82, screen.get_height()-218)),
            '17': interfaceClass.defaultIcon.Icon(position=(186, screen.get_height()-218)),
            '18': interfaceClass.defaultIcon.Icon(position=(290, screen.get_height()-218)),
            '19': interfaceClass.defaultIcon.Icon(position=(394, screen.get_height()-218)),
            '20': interfaceClass.defaultIcon.Icon(position=(498, screen.get_height()-218)),

        }
        
        self.tempitemslot = interfaceClass.defaultIcon.Icon()

        self.prevslot = None
        self.mouseswith = {'0': False, '1': False, '2': False}

    def inventoryRender(self, player):
        if player:
            if player.inventory.opened:
                for key, value in player.inventory.inventoryslots.items():
                    if key:
                        self.inventoryslots[key].iconRender(value)
                self.tempitemslot.iconRender(player.inventory.tempitemslot)
                self.inventoryhided = False
            else:
                for key, value in player.inventory.inventoryslots.items():
                    if key in ['1', '2', '3', '4', '5']:
                        self.inventoryslots[key].iconRender(value)
                self.tempitemslot.iconRender(None)
                self.inventoryhided = True
        else:
            self.inventoryhided = True

        self.inventorySlotsBackground_image.visible(self.inventoryhided)
        self.inventorySlots_image.visible(self.inventoryhided)
        for key, value in self.inventoryslots.items():
            self.inventoryslots[key].visible(self.inventoryhided)

    def quickAccesBarRender(self, player):
        if player:
            match player.inventory.currentslot:
                case None:
                    self.quickAccesBar.imageedit("src/assets/textures/quick_acces_bar_0.png")
                case '1':
                    self.quickAccesBar.imageedit("src/assets/textures/quick_acces_bar_1.png")
                case '2':
                    self.quickAccesBar.imageedit("src/assets/textures/quick_acces_bar_2.png")
                case '3':
                    self.quickAccesBar.imageedit("src/assets/textures/quick_acces_bar_3.png")
                case '4':
                    self.quickAccesBar.imageedit("src/assets/textures/quick_acces_bar_4.png")
                case '5':
                    self.quickAccesBar.imageedit("src/assets/textures/quick_acces_bar_5.png")
            self.quickaccesbarhided = False
        else:
            self.quickaccesbarhided = True
        
        self.quickAccesBar.visible(self.quickaccesbarhided)
        for key, value in self.inventoryslots.items():
            if key in ['1', '2', '3', '4', '5']:
                if value:
                    self.inventoryslots[key].visible(self.quickaccesbarhided)

    def holdedItemRender(self, mouse, mousestate, paused, player):
        #сделать возвышение слоя текущего предмета над другими
        if not paused:
            if player.inventory.opened:
                if mousestate[0]:
                    if not self.mouseswith['0']:
                        if not player.inventory.tempitemslot:
                            for key, value in self.inventoryslots.items():
                                if value.itemicon.rect.collidepoint(mouse):
                                    self.prevslot = key
                                    player.inventory.tempitemslot = player.inventory.inventoryslots[self.prevslot]
                                    player.inventory.inventoryslots[self.prevslot] = None
                                    break
                            self.mouseswith['0'] = True
                    if not self.mouseswith['0']:
                        if player.inventory.tempitemslot:
                            for key, value in self.inventoryslots.items():
                                if value.itemicon.rect.collidepoint(mouse):
                                    if self.prevslot != key:
                                        player.inventory.inventoryslots[key], player.inventory.tempitemslot = player.inventory.tempitemslot, player.inventory.inventoryslots[key]
                                        self.tempitemslot.iconRender(player.inventory.tempitemslot)
                                        self.tempitemslot.moving(mouse)
                                        break
                            else:
                                player.inventory.inventoryslots[self.prevslot], player.inventory.tempitemslot = player.inventory.tempitemslot, player.inventory.inventoryslots[self.prevslot]
                            self.mouseswith['0'] = True
                else:
                    self.mouseswith['0'] = False
                if player.inventory.tempitemslot:
                        self.tempitemslot.moving(mouse)
            else:
                if player.inventory.tempitemslot:
                    player.inventory.inventoryslots[self.prevslot] = player.inventory.tempitemslot
                    player.inventory.tempitemslot = None
        else:
            if player.inventory.tempitemslot:
                player.inventory.inventoryslots[self.prevslot] = player.inventory.tempitemslot
                player.inventory.tempitemslot = None
