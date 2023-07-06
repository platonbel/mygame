import math
from gameCode import interfaceClass, textClass, shapeClass

class Indicator():

    def __init__(self):
        self.hided = False
        self.indicatorBackground = None

    def valueUpdate(self, entity):
        if entity:
            pass
        else:
            pass

    def imageUpdate(self):
        pass

    def positionUpdate(self, position):
        pass
    
    def visibleUpdate(self, hided):
        self.hided = hided

    def get_position(self, side=None):
        return self.indicatorBackground.get_position(side)
    
    def get_width(self):
        return self.indicatorBackground.get_width()
    
    def get_height(self):
        return self.indicatorBackground.get_height()
  
