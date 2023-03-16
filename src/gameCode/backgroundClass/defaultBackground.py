import pygame
import math
from gameCode import shapeClass, backgroundClass

class Background():

    def __init__(self, screen):
        self.backgroundimage = pygame.image.load("src/assets/textures/background.png").convert_alpha()
        self.widthtiles = math.ceil(screen.get_width()/self.backgroundimage.get_width())
        self.heighttiles = math.ceil(screen.get_height()/self.backgroundimage.get_height())

    def tilesRender(self, screen):
        self.widthtiles = math.ceil(screen.get_width()/self.backgroundimage.get_width())
        self.heighttiles = math.ceil(screen.get_height()/self.backgroundimage.get_height())

        for heighttile in range(self.heighttiles):
            for widthtile in range(self.widthtiles):
                screen.blit(self.backgroundimage, (widthtile*self.backgroundimage.get_width(), heighttile*self.backgroundimage.get_height()))

    def update(self, screen):
        self.tilesRender(screen)