import math
from . import defaultIndicatorClass
from gameCode import interfaceClass, textClass, shapeClass

class Indicator(defaultIndicatorClass.Indicator):

    def __init__(self):
        self.hided = False
        self.position = (0, 0)
        self.side = None

        self.reloadingTimeValue = 0
        self.reloadingDelayValue = 0
        self.reloadingRatioValue = 0
        
        self.reloadingBarSizeValue = [384, 12]

        self.indicatorBackground = shapeClass.defaultShape.Shape(image="src/assets/textures/stat_indicator.png", layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        
        self.reloadingBarShape = shapeClass.defaultShape.Shape(headobject=self.indicatorBackground, size=(224, 24), side='topleft', color=(205, 50, 50), layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.reloadingBarText = textClass.defaultText.Text(headobject=self.indicatorBackground, size=36, side='topleft', layer=4, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)

    def valueUpdate(self, entity):
        if entity:
            if entity.inventory.item:
                self.reloadingTimeValue = entity.inventory.item.reloadingtime
                self.reloadingDelayValue = entity.inventory.item.reloadingdelay
                self.reloadingRatioValue = self.reloadingDelayValue/self.reloadingTimeValue if self.reloadingTimeValue >=0 else (0 if self.reloadingTimeValue != math.inf else 0)
            else:
                self.reloadingTimeValue = 0
                self.reloadingDelayValue = 0
                self.reloadingRatioValue = 0
        else:
            self.reloadingTimeValue = 0
            self.reloadingDelayValue = 0
            self.reloadingRatioValue = 0

    def imageUpdate(self):
        self.reloadingBarShape.sizeedit((round(self.reloadingBarSizeValue[0]*self.reloadingRatioValue), self.reloadingBarSizeValue[1]))
        self.reloadingBarText.textedit(f'{round(self.reloadingDelayValue, 1)}%', color=(225, 225, 255))
    
    def positionUpdate(self, position=(0, 0), side=None):
        self.position = position
        self.side = side
        self.indicatorBackground.moving(position, side)
        self.reloadingBarShape.moving((self.reloadingBarShape.headobject.get_position(side='topleft')[0]+416, self.reloadingBarShape.headobject.get_position(side='topleft')[1]+20), side='topleft')
        self.reloadingBarText.moving((self.reloadingBarText.headobject.get_position(side='topleft')[0]+416, self.reloadingBarText.headobject.get_position(side='topleft')[1]+32), side='topleft')
    
    def visibleUpdate(self, entity):
        self.hided = False if entity else True
        self.indicatorBackground.visible(not((not self.hided) and entity.inventory.item.reloading))
        self.reloadingBarShape.visible(not((not self.hided) and entity.inventory.item.reloading))
        self.reloadingBarText.visible(not((not self.hided) and entity.inventory.item.reloading))


  
