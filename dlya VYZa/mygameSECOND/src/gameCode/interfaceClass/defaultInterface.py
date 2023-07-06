
from gameCode import interfaceClass

class Interface():
    def __init__(self, screen):
        self.indicatorsInterface = interfaceClass.indicatorClass.defaultIndicators.Indicators()
        self.inventoryInterface = interfaceClass.inventoryClass.Inventory(screen)
        self.cursorInterface = interfaceClass.cursorClass.Cursor()
        self.pauseInterface = interfaceClass.pauseClass.Pause(screen)

    def update(self, screen, mouse, mouseState, keyState, paused, entity):
        self.indicatorsInterface.update(screen, entity)
        self.inventoryInterface.update(mouse, mouseState, keyState, paused, entity)
        self.cursorInterface.update(mouse, mouseState)
        self.pauseInterface.update(paused)