import pygame
from modules import shapeClass, backgroundClass

class Background():

    def __init__(self):
        backgroundimage = shapeClass.privateShape.Shape(image="src/assets/textures/background.png", position=(0, 0), side='topleft', layer=0, privateLayer=backgroundClass.instances.backgroundLayer.defaultLayer)
