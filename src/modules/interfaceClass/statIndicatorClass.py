import pygame
import math
from modules import interfaceClass, textClass, shapeClass

class Indicator():

    def __init__(self, screen):
        self.hided = False

        self.statIndicator = shapeClass.privateShape.Shape(image="src/assets/textures/stat_indicator.png", position=(screen.get_width()-30, screen.get_height()-30), side='bottomright', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        
        self.healthbar = shapeClass.privateShape.Shape(headobject=self.statIndicator, size=(224, 24), side='topleft', color=(205, 50, 50), layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.staminabar = shapeClass.privateShape.Shape(headobject=self.statIndicator, size=(224, 24), side='topleft', color=(205, 205, 50), layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        
        self.healthvalue = textClass.privateText.Text(headobject=self.statIndicator, size=36, side='topleft', layer=4, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.staminavalue = textClass.privateText.Text(headobject=self.statIndicator, size=36, side='topleft', layer=4, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
    
        self.healthbar.moving((self.healthbar.headobject.rect.topleft[0]+56, self.healthbar.headobject.rect.topleft[1]+20))
        self.staminabar.moving((self.healthbar.headobject.rect.topleft[0]+56, self.healthbar.headobject.rect.topleft[1]+60))
        
        self.healthvalue.moving((self.healthvalue.headobject.rect.topleft[0]+334, self.healthvalue.headobject.rect.topleft[1]+20))
        self.staminavalue.moving((self.staminavalue.headobject.rect.topleft[0]+334, self.staminavalue.headobject.rect.topleft[1]+60))



    def indicatorrender(self, player):
        if player:
            healthratio = player.health / player.maxhealth if player.maxhealth else 0
            staminaratio = player.stamina / player.maxstamina if player.maxstamina else 0

            self.statIndicator.visible(False)
            self.healthbar.visible(False)
            self.staminabar.visible(False)
            self.healthvalue.visible(False)
            self.staminavalue.visible(False)

        else:
            healthratio = 0
            staminaratio = 0
            
            self.statIndicator.visible(True)
            self.healthbar.visible(True)
            self.staminabar.visible(True)
            self.healthvalue.visible(True)
            self.staminavalue.visible(True)
            print(staminaratio, player)
        self.healthbar.sizeedit((round(272*healthratio), 24))
        self.staminabar.sizeedit((round(272*staminaratio), 24))
        
        self.healthvalue.textedit(f'{round((player.health/player.maxhealth if player.maxhealth != math.inf else 1)*100)}%', color=(225, 225, 255))
        self.staminavalue.textedit(f'{round((player.stamina/player.maxstamina if player.maxstamina != math.inf else 1)*100)}%', color=(225, 225, 255))
  
