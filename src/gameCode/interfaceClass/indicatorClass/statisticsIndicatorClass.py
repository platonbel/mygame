import math
from . import defaultIndicatorClass
from gameCode import interfaceClass, textClass, shapeClass

class Indicator(defaultIndicatorClass.Indicator):

    def __init__(self):
        self.hided = False
        self.position = (0, 0)
        self.side = None

        self.healthValue = 0
        self.staminaValue = 0
        self.maxhealthValue = 0
        self.maxstaminaValue = 0
        self.healthRatioValue = 0
        self.staminaRatioValue = 0

        self.healthBarSizeValue = [272, 24]
        self.staminaBarSizeValue = [272, 24]

        self.indicatorBackground = shapeClass.defaultShape.Shape(image="src/assets/textures/stat_indicator.png", layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        
        self.healthBarShape = shapeClass.defaultShape.Shape(headobject=self.indicatorBackground, size=(224, 24), side='topleft', color=(205, 50, 50), layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.staminaBarShape = shapeClass.defaultShape.Shape(headobject=self.indicatorBackground, size=(224, 24), side='topleft', color=(205, 205, 50), layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer) 
        self.healthBarText = textClass.defaultText.Text(headobject=self.indicatorBackground, size=36, side='center', layer=4, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.staminaBarText = textClass.defaultText.Text(headobject=self.indicatorBackground, size=36, side='center', layer=4, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)

    def valueUpdate(self, entity):
        if entity:
            self.healthValue = entity.health
            self.maxhealthValue = entity.maxhealth
            self.staminaValue = entity.stamina
            self.maxstaminaValue = entity.maxstamina
            self.healthRatioValue = entity.health / entity.maxhealth if entity.maxhealth >= 0 else (1 if entity.maxhealth != math.inf else 0)
            self.staminaRatioValue = entity.stamina / entity.maxstamina if entity.maxstamina >= 0 else (1 if entity.maxhealth != math.inf else 0)
        else:
            self.healthValue = 0
            self.maxhealthValue = 0
            self.staminaValue = 0
            self.maxstaminaValue = 0
            self.healthRatioValue = 0
            self.staminaRatioValue = 0

    def imageUpdate(self):
        self.healthBarShape.sizeedit((round(self.healthBarSizeValue[0]*self.healthRatioValue), self.healthBarSizeValue[1]))
        self.staminaBarShape.sizeedit((round(self.healthBarSizeValue[0]*self.staminaRatioValue), self.staminaBarSizeValue[1]))
        
        self.healthBarText.textedit(f'{round(self.healthRatioValue*100)}%', color=(225, 225, 255))
        self.staminaBarText.textedit(f'{round(self.staminaRatioValue*100)}%', color=(225, 225, 255))

    def positionUpdate(self, position, side):
        self.position = position
        self.side = side
        self.indicatorBackground.moving(self.position, self.side)
        self.healthBarShape.moving((self.healthBarShape.headobject.get_position(side='topleft')[0]+416, self.healthBarShape.headobject.get_position(side='topleft')[1]+20), side='topleft')
        self.staminaBarShape.moving((self.staminaBarShape.headobject.get_position(side='topleft')[0]+416, self.staminaBarShape.headobject.get_position(side='topleft')[1]+60), side='topleft')
        self.healthBarText.moving((self.healthBarText.headobject.get_position(side='topleft')[0]+416, self.healthBarText.headobject.get_position(side='topleft')[1]+32), side='topleft')
        self.staminaBarText.moving((self.staminaBarText.headobject.get_position(side='topleft')[0]+416, self.staminaBarText.headobject.get_position(side='topleft')[1]+72), side='topleft')
    
    def visibleUpdate(self, entity):
        self.hided = False if entity else True
        self.indicatorBackground.visible(self.hided)
        self.healthBarShape.visible(self.hided)
        self.staminaBarShape.visible(self.hided)
        self.healthBarText.visible(self.hided)
        self.staminaBarText.visible(self.hided)
