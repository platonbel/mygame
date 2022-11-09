
from modules import interfaceClass

class Interface():
    def __init__(self, screen):
        self.statIndicatorInterface = interfaceClass.statIndicatorClass.Indicator(screen)
        self.itemIndecatorInterface = interfaceClass.itemIndicatorClass.Indicator(screen)
        self.quickAccesBarInterface = interfaceClass.quickAccesBarClass.QuickAccesBar(screen)
        self.inventoryInterface = interfaceClass.inventoryClass.Inventory(screen)
        self.cursorInterface = interfaceClass.cursorClass.Cursor()
        self.pauseInterface = interfaceClass.pauseClass.Pause(screen)

    def update(self, mouse, mousestate, keystate, paused, player):
        self.statIndicatorInterface.indicatorrender(player)
        self.itemIndecatorInterface.indicatorrender(player)
        self.quickAccesBarInterface.quickAccesBarRender(player)
        self.inventoryInterface.inventoryRender(player)
        self.cursorInterface.cursorrender(mouse, mousestate)
        self.pauseInterface.pauserender(paused)