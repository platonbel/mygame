import pygame
from modules import interfaceClass, shapeClass


class QuickAccesBar():

    def __init__(self, screen):
        self.hided = True
        self.barslots = {
            '1': shapeClass.privateShape.Shape(position=(84, screen.get_height()-84), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            '2': shapeClass.privateShape.Shape(position=(188, screen.get_height()-84), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            '3': shapeClass.privateShape.Shape(position=(292, screen.get_height()-84), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            '4': shapeClass.privateShape.Shape(position=(396, screen.get_height()-84), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            '5': shapeClass.privateShape.Shape(position=(500, screen.get_height()-84), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        }
        self.quickAccesBar = shapeClass.privateShape.Shape(image="src/assets/textures/quick_acces_bar_0.png", position=(30, screen.get_height()-30), side='bottomleft', layer=1, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)

    def quickAccesBarRender(self, player):
        if player:
            match player.quickAccesBar.currentslot:
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

            for key, value in player.quickAccesBar.barslots.items():
                if value != None:
                    self.barslots[key].imageedit(player.quickAccesBar.barslots[key].itemicon)

            self.hided = False
        else:
            self.hided = True
        
        self.quickAccesBar.hided = self.hided