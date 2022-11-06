import  pygame
from modules import shapeClass, interfaceClass

class Cursor():
    def __init__(self):
        self.cursor = shapeClass.privateShape.Shape(image="src/assets/textures/cursor_0.png", position=(0, 0), side='topleft', layer=7, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        pygame.mouse.set_visible(False)

    def cursorrender(self, mouse, mousestate):
        self.cursor.position = mouse
        if mousestate[0]:
            self.cursor.imageedit("src/assets/textures/cursor_1.png")
        else:
            self.cursor.imageedit("src/assets/textures/cursor_0.png")