from modules import textClass, interfaceClass, shapeClass

class Pause():
    def __init__(self, screen):
        self.shadeground = shapeClass.privateShape.Shape(size=screen.get_size(), position=(0, 0), side='topleft', color=(0, 0, 0), alpha=75, layer=5, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.pauselabel = textClass.privateText.Text(text='PAUSE', size=72, position=(screen.get_width()//2, screen.get_height()//2), side='center', layer=6, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)

    def pauserender(self, paused):
        if paused:
            self.shadeground.hided = False
            self.pauselabel.hided = False
        else:
            self.shadeground.hided = True
            self.pauselabel.hided = True