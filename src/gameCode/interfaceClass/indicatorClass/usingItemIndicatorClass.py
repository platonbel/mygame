import math
from . import defaultIndicatorClass
from gameCode import interfaceClass, textClass, shapeClass

class Indicator(defaultIndicatorClass.Indicator):

    def __init__(self):
        self.hided = False
        self.position = (0, 0)
        self.side = None

        self.usingTimeValue = 0
        self.usingDelayValue = 0
        self.usingRatioValue = 0
        
        self.usingBarSizeValue = [384, 12]

        self.indicatorBackground = shapeClass.defaultShape.Shape(image="src/assets/textures/stat_indicator.png", layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        
        self.usingBarShape = shapeClass.defaultShape.Shape(headobject=self.indicatorBackground, size=(224, 24), side='topleft', color=(205, 50, 50), layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.usingBarText = textClass.defaultText.Text(headobject=self.indicatorBackground, size=36, side='topleft', layer=4, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)

    def valueUpdate(self, entity):
        if entity:
            if entity.inventory.item:
                self.usingTimeValue = entity.inventory.item.usingTimeValue
                self.usingDelayValue = entity.inventory.item.usingDelayValue
                self.usingRatioValue = self.usingDelayValue/self.usingTimeValue if self.usingTimeValue >=0 else (0 if self.usingTimeValue != math.inf else 0)
            else:
                self.usingTimeValue = 0
                self.usingDelayValue = 0
                self.usingRatioValue = 0
        else:
            self.usingTimeValue = 0
            self.usingDelayValue = 0
            self.usingRatioValue = 0

    def imageUpdate(self):
        self.usingBarShape.sizeedit((round(self.usingBarSizeValue[0]*self.usingRatioValue), self.usingBarSizeValue[1]))
        self.usingBarText.textedit(f'{round(self.usingDelayValue, 1)}%', color=(225, 225, 255))
    
    def positionUpdate(self, position=(0, 0), side=None):
        self.position = position
        self.side = side
        self.indicatorBackground.moving(position, side)
        self.usingBarShape.moving((self.usingBarShape.headobject.get_position(side='topleft')[0]+416, self.usingBarShape.headobject.get_position(side='topleft')[1]+20), side='topleft')
        self.usingBarText.moving((self.usingBarText.headobject.get_position(side='topleft')[0]+416, self.usingBarText.headobject.get_position(side='topleft')[1]+32), side='topleft')
    
    def visibleUpdate(self, entity):
        self.hided = False if entity else True
        self.indicatorBackground.visible(not((not self.hided) and entity.inventory.item.using))
        self.usingBarShape.visible(not((not self.hided) and entity.inventory.item.using))
        self.usingBarText.visible(not((not self.hided) and entity.inventory.item.using))

  
