from gameCode import chhh, interfaceClass

class Pause():
    def __init__(self, screen):
        self.shadeGround = chhh.defaultShape.Shape(name='shadeground', imageLink="src/assets/textures/shadeground.png", position=(0, 0), side='topleft', alpha=255, mainObjectLink=None, layer=5, shapeGroup=interfaceClass.instances.interfaceGroup.defaultGroup, shapeLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.pauseLabel = chhh.defaultTitle.Text(name='pauselabel', text='PAUSE', size=72, position=(screen.get_width()//2, screen.get_height()//2), side='center', layer=6, shapeGroup=interfaceClass.instances.interfaceGroup.defaultGroup, shapeLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.shadeGround.size_edit(screen.get_size())
        self.visible = True

    def update(self, paused):
        if paused:
            self.visible = False
            self.shadeGround.visible_edit(self.visible)
            self.pauseLabel.visible_edit(self.visible)
        else:
            self.visible = True
            self.shadeGround.visible_edit(self.visible)
            self.pauseLabel.visible_edit(self.visible)