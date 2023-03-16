from gameCode import interfaceClass

class Indicators():

    def __init__(self):
        self.side = 'bottomright'
        self.position = (0, 0)
        self.hided = False

        self.statisticsIndicator = interfaceClass.indicatorClass.statisticsIndicatorClass.Indicator()
        self.itemIndicator = interfaceClass.indicatorClass.itemIndicatorClass.Indicator()
        self.pickingItemIndicator = interfaceClass.indicatorClass.pickingItemIndicatorClass.Indicator()
        self.usingItemIndicator = interfaceClass.indicatorClass.usingItemIndicatorClass.Indicator()
        self.reloadingItemIndicator = interfaceClass.indicatorClass.reloadingItemIndicatorClass.Indicator()

        self.indicatorsGroup= {
            'statisticsIndicator': self.statisticsIndicator, 
            'pickingItemIndicator': self.pickingItemIndicator,
            'itemIndicator': self.itemIndicator,
            'usingItemIndicator': self.usingItemIndicator,
            'reloadingItemIndicator': self.reloadingItemIndicator
        }

    def valueUpdate(self, entity):
        self.statisticsIndicator.valueUpdate(entity)
        self.itemIndicator.valueUpdate(entity)
        self.pickingItemIndicator.valueUpdate(entity)
        self.usingItemIndicator.valueUpdate(entity)
        self.reloadingItemIndicator.valueUpdate(entity)

    def imageUpdate(self):
        self.statisticsIndicator.imageUpdate()
        self.itemIndicator.imageUpdate()
        self.pickingItemIndicator.imageUpdate()
        self.usingItemIndicator.imageUpdate()
        self.reloadingItemIndicator.imageUpdate()

    def visibleUpdate(self, entity):
        self.statisticsIndicator.visibleUpdate(entity)
        self.itemIndicator.visibleUpdate(entity)
        self.pickingItemIndicator.visibleUpdate(entity)
        self.usingItemIndicator.visibleUpdate(entity)
        self.reloadingItemIndicator.visibleUpdate(entity)

    def positionUpdate(self, screen):
        prevIndicator = None
        for indicator in self.indicatorsGroup.values():
            if not indicator.hided:
                if prevIndicator:
                    self.position = prevIndicator.get_position(side=self.side)[0], prevIndicator.get_position(side=self.side)[1]-prevIndicator.get_height()
                else:
                    self.position = screen.get_width()-30, screen.get_height()-30
                indicator.positionUpdate(self.position, self.side)
                prevIndicator = indicator
        

    def update(self, screen, entity):
        self.valueUpdate(entity)
        self.imageUpdate()
        self.positionUpdate(screen)
        self.visibleUpdate(entity)
