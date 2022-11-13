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

            '1': (shapeClass.privateShape.Shape(position=(82, screen.get_height()-82), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '2': (shapeClass.privateShape.Shape(position=(186, screen.get_height()-82), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '3': (shapeClass.privateShape.Shape(position=(290, screen.get_height()-82), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '4': (shapeClass.privateShape.Shape(position=(394, screen.get_height()-82), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '5': (shapeClass.privateShape.Shape(position=(498, screen.get_height()-82), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer),
            textClass.privateText.Text(side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),

            '6': (shapeClass.privateShape.Shape(position=(82, screen.get_height()-426), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '7': (shapeClass.privateShape.Shape(position=(186, screen.get_height()-426), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '8': (shapeClass.privateShape.Shape(position=(290, screen.get_height()-426), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '9': (shapeClass.privateShape.Shape(position=(394, screen.get_height()-426), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '10': (shapeClass.privateShape.Shape(position=(498, screen.get_height()-426), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer),
            textClass.privateText.Text(side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
        
            '11': (shapeClass.privateShape.Shape(position=(82, screen.get_height()-322), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '12': (shapeClass.privateShape.Shape(position=(186, screen.get_height()-322), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '13': (shapeClass.privateShape.Shape(position=(290, screen.get_height()-322), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '14': (shapeClass.privateShape.Shape(position=(394, screen.get_height()-322),side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '15': (shapeClass.privateShape.Shape(position=(498, screen.get_height()-322), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '16': (shapeClass.privateShape.Shape(position=(82, screen.get_height()-218), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer),
            textClass.privateText.Text(side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)), 

            '17': (shapeClass.privateShape.Shape(position=(186, screen.get_height()-218), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer),
            textClass.privateText.Text(side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),

            '18': (shapeClass.privateShape.Shape(position=(290, screen.get_height()-218), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '19': (shapeClass.privateShape.Shape(position=(394, screen.get_height()-218), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '20': (shapeClass.privateShape.Shape(position=(498, screen.get_height()-218), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
        }
        
        self.tempitemslot = (shapeClass.privateShape.Shape(side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer))


        self.prevslot = None
        self.mouseswith = {'0': False, '1': False, '2': False}

    def inventoryRender(self, player):
        if player:
            if player.inventory.opened:
                for key, value in player.inventory.inventoryslots.items():
                    if key:
                        if value:
                            self.inventoryslots[key][0].imageedit(value.itemicon)
                            self.inventoryslots[key][1].position = (self.inventoryslots[key][0].position[0]+32, self.inventoryslots[key][0].position[1]+32)

                            match value.itemtype:
                                case 'ammunition':
                                    self.inventoryslots[key][1].textedit(str(value.amount), (0, 0, 0))
                                case _:
                                    self.inventoryslots[key][1].textedit(None, (0, 0, 0))  
                        else:
                            self.inventoryslots[key][0].imageedit("src/assets/textures/empty_icon.png")
                            self.inventoryslots[key][1].textedit(None, (0, 0, 0))
        
                if player.inventory.tempitemslot:
                    self.tempitemslot[0].imageedit(player.inventory.tempitemslot.itemicon)
                    match player.inventory.tempitemslot.itemtype:
                        case 'ammunition':
                            self.tempitemslot[1].textedit(str(player.inventory.tempitemslot.amount), (0, 0, 0))
                        case _:
                            self.tempitemslot[1].textedit(None, (0, 0, 0))
                    self.tempitemslot[0].position = self.inventoryslots[self.prevslot][0].position
                    self.tempitemslot[1].position = (self.tempitemslot[0].position[0]+32, self.tempitemslot[0].position[1]+32)
                else:
                    self.tempitemslot[0].imageedit("src/assets/textures/empty_icon.png")
                    self.tempitemslot[1].textedit(None, (0, 0, 0))
                self.inventoryhided = False
            else:
                for key, value in player.inventory.inventoryslots.items():
                    if key in ['1', '2', '3', '4', '5']:
                        if value:
                            self.inventoryslots[key][1].position = (self.inventoryslots[key][0].position[0]+32, self.inventoryslots[key][0].position[1]+32)
                            self.inventoryslots[key][0].imageedit(value.itemicon)
                            match value.itemtype:
                                case 'ammunition':
                                    self.inventoryslots[key][1].textedit(str(value.amount), (0, 0, 0))
                                case _:
                                    self.inventoryslots[key][1].textedit(None, (0, 0, 0))  
                        else:
                            self.inventoryslots[key][0].imageedit("src/assets/textures/empty_icon.png")
                            self.inventoryslots[key][1].textedit(None, (0, 0, 0))
                self.tempitemslot[0].imageedit("src/assets/textures/empty_icon.png")
                self.tempitemslot[1].textedit(None, (0, 0, 0))
                self.inventoryhided = True
        else:
            self.inventoryhided = True

        self.inventorySlotsBackground_image.hided = self.inventoryhided
        self.inventorySlots_image.hided = self.inventoryhided
        for key, value in self.inventoryslots.items():
            self.inventoryslots[key][0].hided = self.inventoryhided
            self.inventoryslots[key][1].hided = self.inventoryhided

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
        
        self.quickAccesBar.hided = self.quickaccesbarhided
        for key, value in self.inventoryslots.items():
            if key in ['1', '2', '3', '4', '5']:
                if value:
                    self.inventoryslots[key][0].hided = self.quickaccesbarhided
                    self.inventoryslots[key][1].hided = self.quickaccesbarhided

    def holdedItemRender(self, mouse, mousestate, paused, player):
        #сделать возвышение слоя текущего предмета над другими
        if not paused:
            if player.inventory.opened:
                if mousestate[0]:
                    if not self.mouseswith['0']:
                        if not player.inventory.tempitemslot:
                            for key, value in self.inventoryslots.items():
                                if value[0].rect.collidepoint(mouse):
                                    self.prevslot = key
                                    player.inventory.tempitemslot = player.inventory.inventoryslots[self.prevslot]
                                    player.inventory.inventoryslots[self.prevslot] = None
                                    break
                            self.mouseswith['0'] = True
                    if not self.mouseswith['0']:
                        if player.inventory.tempitemslot:
                            for key, value in self.inventoryslots.items():
                                if value[0].rect.collidepoint(mouse):
                                    if self.prevslot != key:
                                        player.inventory.inventoryslots[key], player.inventory.tempitemslot = player.inventory.tempitemslot, player.inventory.inventoryslots[key]
                                        self.tempitemslot[0].imageedit(player.inventory.tempitemslot.itemicon if player.inventory.tempitemslot else "src/assets/textures/empty_icon.png") 
                                        self.tempitemslot[0].position = mouse
                                        self.tempitemslot[1].position = (self.tempitemslot[0].position[0]+32, self.tempitemslot[0].position[1]+32)
                                        break
                            else:
                                player.inventory.inventoryslots[self.prevslot], player.inventory.tempitemslot = player.inventory.tempitemslot, player.inventory.inventoryslots[self.prevslot]
                            self.mouseswith['0'] = True
                else:
                    self.mouseswith['0'] = False
                if player.inventory.tempitemslot:
                        self.tempitemslot[0].position = mouse
                        self.tempitemslot[1].position = (self.tempitemslot[0].position[0]+32, self.tempitemslot[0].position[1]+32)
            else:
                if player.inventory.tempitemslot:
                    player.inventory.inventoryslots[self.prevslot] = player.inventory.tempitemslot
                    player.inventory.tempitemslot = None
        else:
            if player.inventory.tempitemslot:
                player.inventory.inventoryslots[self.prevslot] = player.inventory.tempitemslot
                player.inventory.tempitemslot = None
