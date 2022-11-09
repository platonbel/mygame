import pygame
from modules import interfaceClass, shapeClass, textClass


class QuickAccesBar():

    def __init__(self, screen):
        self.hided = True
        self.barslots = {
            '1': (shapeClass.privateShape.Shape(position=(82, screen.get_height()-82), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(position=(114, screen.get_height()-50), side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '2': (shapeClass.privateShape.Shape(position=(186, screen.get_height()-82), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(position=(218, screen.get_height()-50), side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '3': (shapeClass.privateShape.Shape(position=(290, screen.get_height()-82), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(position=(324, screen.get_height()-50), side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '4': (shapeClass.privateShape.Shape(position=(394, screen.get_height()-82), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer), 
            textClass.privateText.Text(position=(426, screen.get_height()-50), side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)),
            
            '5': (shapeClass.privateShape.Shape(position=(498, screen.get_height()-82), side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer),
            textClass.privateText.Text(position=(530, screen.get_height()-50), side = 'bottomright', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer))
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
                if key:
                    if value:
                        self.barslots[key][0].imageedit(value.itemicon)
                        if value.itemtype == 'ammunition':
                            self.barslots[key][1].textedit(str(value.amount), (0, 0, 0))
                    else:
                        self.barslots[key][0].imageedit("src/assets/textures/empty_icon.png")
                        self.barslots[key][1].textedit(None, (0, 0, 0))

            self.hided = False
        else:
            self.hided = True
        
        self.quickAccesBar.hided = self.hided
        for key, value in self.barslots.items():
            if value:
                self.barslots[key][0].hided = self.hided
                self.barslots[key][1].hided = self.hided