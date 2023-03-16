import math
from . import defaultIndicatorClass
from gameCode import interfaceClass, textClass, shapeClass

class Indicator(defaultIndicatorClass.Indicator):

    def __init__(self):
        self.hided = False
        self.position = (0, 0)
        self.side = None

        self.pickingTimeValue = 0
        self.pickingDelayValue = 0
        self.pickingRatioValue = 0
        
        self.pickingBarSizeValue = [384, 12]

        self.indicatorBackground = shapeClass.defaultShape.Shape(image="src/assets/textures/stat_indicator.png", layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        
        self.pickingBarShape = shapeClass.defaultShape.Shape(headobject=self.indicatorBackground, size=(224, 24), side='topleft', color=(205, 50, 50), layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.pickingBarText = textClass.defaultText.Text(headobject=self.indicatorBackground, size=36, side='topleft', layer=4, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)

    def valueUpdate(self, entity):
        if entity:
            if entity.inventory.item:
                self.pickingTimeValue = entity.inventory.item.pickingtime
                self.pickingDelayValue = entity.inventory.item.pickingdelay
                self.pickingRatioValue = self.pickingDelayValue/self.pickingTimeValue if self.pickingTimeValue >=0 else (0 if self.pickingTimeValue != math.inf else 0)
            else:
                self.pickingTimeValue = 0
                self.pickingDelayValue = 0
                self.pickingRatioValue = 0
        else:
            self.pickingTimeValue = 0
            self.pickingDelayValue = 0
            self.pickingRatioValue = 0

    def imageUpdate(self):
        self.pickingBarShape.sizeedit((round(self.pickingBarSizeValue[0]*self.pickingRatioValue), self.pickingBarSizeValue[1]))
        self.pickingBarText.textedit(f'{round(self.pickingDelayValue, 1)}%', color=(225, 225, 255))
    
    def positionUpdate(self, position=(0, 0), side=None):
        self.position = position
        self.side = side
        self.indicatorBackground.moving(position, side)
        self.pickingBarShape.moving((self.pickingBarShape.headobject.get_position(side='topleft')[0]+416, self.pickingBarShape.headobject.get_position(side='topleft')[1]+20), side='topleft')
        self.pickingBarText.moving((self.pickingBarText.headobject.get_position(side='topleft')[0]+416, self.pickingBarText.headobject.get_position(side='topleft')[1]+32), side='topleft')
    
    def visibleUpdate(self, entity):
        self.hided = False if entity else True
        self.indicatorBackground.visible(not((not self.hided) and entity.inventory.item.picking))
        self.pickingBarShape.visible(not((not self.hided) and entity.inventory.item.picking))
        self.pickingBarText.visible(not((not self.hided) and entity.inventory.item.picking))

  
