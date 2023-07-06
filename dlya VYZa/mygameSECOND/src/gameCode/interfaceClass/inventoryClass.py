import pygame
import copy
import math
from gameCode import interfaceClass, shapeClass, textClass, functions

class Inventory():

    def __init__(self, screen):
        self.inventoryhided = True
        self.quickaccesbarhided = True

        self.inventorySlotsBackground_image = shapeClass.defaultShape.Shape(image="src/assets/textures/inventory_slots_background.png", position=(22, screen.get_height()-22), side='bottomleft', layer=0, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.inventorySlots_image = shapeClass.defaultShape.Shape(image="src/assets/textures/inventory_slots.png", position=(30, screen.get_height()-166), side='bottomleft', layer=1, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.quickAccesBar = shapeClass.defaultShape.Shape(image="src/assets/textures/quick_acces_bar_0.png", position=(30, screen.get_height()-30), side='bottomleft', layer=1, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)

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

        self.mouseswitch = {'0': False, '1': False, '2': False}
        self.keyswitch = {'K_LSHIFT': False}

    def inventoryRender(self, player):
        #render item icons for slots in inventory
        self.inventoryhided = False if player.inventory.opened else True
        self.quickaccesbarhided = False if not player.inventory.opened else True
        for key, value in player.inventory.inventoryslots.items():
            if key:
                self.inventoryslots[key].iconRender(value)
                if key in ['1', '2', '3', '4', '5']:
                    self.inventoryslots[key].visible(not(self.inventoryhided or self.quickaccesbarhided))
                else:
                    self.inventoryslots[key].visible(self.inventoryhided)
        #render quickbar texture
        match player.inventory.currentslot:
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
            case _:
                self.quickAccesBar.imageedit("src/assets/textures/quick_acces_bar_0.png")

        self.inventorySlotsBackground_image.visible(self.inventoryhided)
        self.inventorySlots_image.visible(self.inventoryhided)
        self.quickAccesBar.visible(not(self.inventoryhided or self.quickaccesbarhided))

    def holdedItemRender(self, mouse, mousestate, keystate, paused, player):
        #сделать возвышение слоя текущего предмета над другими
        if not paused:  
            if player.inventory.opened:
                if mousestate[0]:
                    if not self.mouseswitch['0']:
                        #check collide with inventory slots
                        for key, value in self.inventoryslots.items():
                            if value:
                                if value.itemicon.rect.collidepoint(mouse):
                                    player.inventory.currenttempslot = key
                                    break
                        else:
                            player.inventory.currenttempslot = None

                        #take/take off
                        if player.inventory.currenttempslot:
                            if player.inventory.inventoryslots[player.inventory.currenttempslot] and functions.checkEquivalence(player.inventory.inventoryslots[player.inventory.currenttempslot], player.inventory.tempitem) and player.inventory.inventoryslots[player.inventory.currenttempslot].stackable: 
                                player.inventory.inventoryslots[player.inventory.currenttempslot].amount += player.inventory.tempitem.amount
                                player.inventory.tempitem = None
                            else:
                                player.inventory.tempitem, player.inventory.inventoryslots[player.inventory.currenttempslot] = player.inventory.inventoryslots[player.inventory.currenttempslot], player.inventory.tempitem
                        
                        else:
                            if player.inventory.tempitem:
                                emptyslot = functions.founditem(player.inventory.inventoryslots, None)
                                aviableslot = functions.founditem(player.inventory.inventoryslots, player.inventory.tempitem)
                                if aviableslot[0] and aviableslot[1]:
                                    if aviableslot[1].stackable:
                                        player.inventory.inventoryslots[aviableslot[0]].amount += player.inventory.tempitem.amount
                                        player.inventory.tempitem = None
                                    elif emptyslot[0]:
                                        player.inventory.tempitem, player.inventory.inventoryslots[emptyslot[0]] = player.inventory.inventoryslots[emptyslot[0]], player.inventory.tempitem
                                elif emptyslot[0]:
                                    player.inventory.tempitem, player.inventory.inventoryslots[emptyslot[0]] = player.inventory.inventoryslots[emptyslot[0]], player.inventory.tempitem
                                
                                if not (aviableslot[0] and emptyslot[0]):
                                    #Nothing, but i can make items on floor
                                    player.inventory.tempitem = None

                        self.tempitemslot.moving(mouse) 
                        self.tempitemslot.iconRender(player.inventory.tempitem)
                        self.mouseswitch['0'] = True
                else:
                    self.mouseswitch['0'] = False

                if mousestate[2]:
                    if not self.mouseswitch['2']:
                        if not player.inventory.tempitem:
                            for key, value in self.inventoryslots.items():
                                if value:
                                    if value.itemicon.rect.collidepoint(mouse):
                                        player.inventory.currenttempslot = key
                                        break
                            else:
                                player.inventory.currenttempslot = None

                            if player.inventory.currenttempslot:
                                if player.inventory.inventoryslots[player.inventory.currenttempslot]:
                                    if player.inventory.inventoryslots[player.inventory.currenttempslot].stackable:
                                        print(player.inventory.inventoryslots[player.inventory.currenttempslot])
                                        player.inventory.tempitem = copy.deepcopy(player.inventory.inventoryslots[player.inventory.currenttempslot])#######
                                        player.inventory.tempitem.amount = math.ceil(player.inventory.inventoryslots[player.inventory.currenttempslot].amount/2)
                                        player.inventory.inventoryslots[player.inventory.currenttempslot].amount -= player.inventory.tempitem.amount
                                    else:
                                        player.inventory.inventoryslots[player.inventory.currenttempslot], player.inventory.tempitem = None, player.inventory.inventoryslots[player.inventory.currenttempslot]
                        else:
                            for key, value in self.inventoryslots.items():
                                if value:
                                    if value.itemicon.rect.collidepoint(mouse):
                                        player.inventory.currenttempslot = key
                                        break
                            else:
                                player.inventory.currenttempslot = None

                            if player.inventory.currenttempslot:
                                if player.inventory.inventoryslots[player.inventory.currenttempslot]:
                                    if functions.checkEquivalence(player.inventory.inventoryslots[player.inventory.currenttempslot], player.inventory.tempitem) and player.inventory.inventoryslots[player.inventory.currenttempslot].stackable:
                                        player.inventory.inventoryslots[player.inventory.currenttempslot].amount += 1
                                        player.inventory.tempitem.amount -= 1
                                else:
                                    if player.inventory.tempitem.stackable:
                                        player.inventory.inventoryslots[player.inventory.currenttempslot] = copy.deepcopy(player.inventory.tempitem)
                                        player.inventory.inventoryslots[player.inventory.currenttempslot].amount =1
                                        player.inventory.tempitem.amount -= 1
                                    else:
                                        player.inventory.inventoryslots[player.inventory.currenttempslot], player.inventory.tempitem = player.inventory.tempitem, None
                        self.mouseswitch['2'] = True
                else:
                    self.mouseswitch['2'] = False


                if player.inventory.tempitem:
                    self.tempitemslot.moving(mouse)
                    self.tempitemslot.iconRender(player.inventory.tempitem)
                else:
                    self.tempitemslot.iconRender(None)
            else:
                if player.inventory.tempitem:
                    key, value = functions.founditem(player.inventory.inventoryslots, None)
                    player.inventory.inventoryslots[key], player.inventory.tempitem = player.inventory.tempitem, None
                    self.tempitemslot.iconRender(player.inventory.tempitem)
        else:
            if player.inventory.tempitem:
                key, value = functions.founditem(player.inventory.inventoryslots, None)
                player.inventory.inventoryslots[key], player.inventory.tempitem = player.inventory.tempitem, None
                self.tempitemslot.iconRender(player.inventory.tempitem)

    def update(self, mouse, mousestate, keystate, paused, player):
        self.inventoryRender(player)
        self.holdedItemRender(mouse, mousestate, keystate, paused, player)

        
