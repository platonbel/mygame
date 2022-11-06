import pygame
import math
from modules import interfaceClass, textClass, shapeClass

class Indicator():

    def __init__(self, screen):
        self.visible = True

        #
        self.statIndicator = shapeClass.privateShape.Shape(image="src/assets/textures/stat_indicator.png", position=(screen.get_width()-30, screen.get_height()-30), side='bottomright', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.healthbar = shapeClass.privateShape.Shape(headobject=self.statIndicator, size=(224, 24), side='topleft', color=(205, 50, 50), layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.staminabar = shapeClass.privateShape.Shape(headobject=self.statIndicator, size=(224, 24), side='topleft', color=(205, 205, 50), layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        
        self.healthvalue = textClass.privateText.Text(headobject=self.statIndicator, size=36, side='topleft', layer=4, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.staminavalue = textClass.privateText.Text(headobject=self.statIndicator, size=36, side='topleft', layer=4, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
    




    def indicatorrender(self, player=None):
        if player != None:

            healthratio = player.health / player.maxhealth
            energyratio = player.energy / player.maxenergy

            self.healthbar.position = (self.healthbar.headobject.rect.topleft[0]+56, self.healthbar.headobject.rect.topleft[1]+20)
            self.staminabar.position = (self.healthbar.headobject.rect.topleft[0]+56, self.healthbar.headobject.rect.topleft[1]+60)
            
            self.healthvalue.position = (self.healthvalue.headobject.rect.topleft[0]+302, self.healthvalue.headobject.rect.topleft[1]+20)
            self.staminavalue.position = (self.staminavalue.headobject.rect.topleft[0]+302, self.staminavalue.headobject.rect.topleft[1]+60)

            self.healthbar.sizeedit((round(240*healthratio), 24))
            self.staminabar.sizeedit((round(240*energyratio), 24))
            
            self.healthvalue.textedit(f'{round((player.health/player.maxhealth if player.maxhealth != math.inf else 1)*100)}%', color=(225, 225, 255))
            self.staminavalue.textedit(f'{round((player.energy/player.maxenergy if player.maxenergy != math.inf else 1)*100)}%', color=(225, 225, 255))

            self.hided = False

        else:
            self.hided = True

        self.statIndicator.hided = self.hided
        self.healthbar.hided = self.hided
        self.staminabar.hided = self.hided
        self.healthvalue.hided = self.hided
        self.staminavalue.hided = self.hided
  
