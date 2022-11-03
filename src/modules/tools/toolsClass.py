import pygame
import math
from modules import entityClass, textClass, shapeClass, tools

class Interface():

    def __init__(self, screen):
        self.healthIndicator = textClass.privateText.Text(position=(screen.get_width()-60, screen.get_height()-120), side='bottomright', layer=0, private=tools.instances.toolsLayer.interfaceLayer)
        self.staminaIndicator = textClass.privateText.Text(position=(screen.get_width()-60, screen.get_height()-90), side='bottomright', layer=0, private=tools.instances.toolsLayer.interfaceLayer)
        self.ammoIndicator = textClass.privateText.Text(position=(screen.get_width()-60, screen.get_height()-60), side='bottomright', layer=0, private=tools.instances.toolsLayer.interfaceLayer)

        self.ammunitionIndicator = textClass.privateText.Text(position=(screen.get_width()-60, screen.get_height()-300), side='bottomright', layer=0, private=tools.instances.toolsLayer.interfaceLayer)
        self.assaultRiffleAmmunitionIndicator = textClass.privateText.Text(position=(screen.get_width()-60, screen.get_height()-270), side='bottomright', layer=0, private=tools.instances.toolsLayer.interfaceLayer)
        self.shotgunAmmunitionIndicator = textClass.privateText.Text(position=(screen.get_width()-60, screen.get_height()-240), side='bottomright', layer=0, private=tools.instances.toolsLayer.interfaceLayer)
        self.pistolAmmunitionIndicator = textClass.privateText.Text(position=(screen.get_width()-60, screen.get_height()-210), side='bottomright', layer=0, private=tools.instances.toolsLayer.interfaceLayer)

        self.pauselabel = textClass.privateText.Text(text='PAUSE', size=72, position=(screen.get_width()//2, screen.get_height()//2), side='center', layer=2, private=tools.instances.toolsLayer.interfaceLayer)

        self.shadeground = shapeClass.privateShape.Shape(size=screen.get_size(), position=(0, 0), side='topleft', color=(0, 0, 0), alpha=75, layer=1, private=tools.instances.toolsLayer.interfaceLayer)

        self.cursor = entityClass.cursorEntity.Cursor(layer=3, private=tools.instances.toolsLayer.interfaceLayer)

    def cursorrender(self):
        None

    def indicators(self, player):
        self.healthIndicator.textedit(f'Health: {round((player.health/player.maxhealth if player.maxhealth != math.inf else 1)*100)}%', (205, 50, 50))
        self.staminaIndicator.textedit(f'Stamina: {round((player.energy/player.maxenergy if player.maxenergy != math.inf else 1)*100)}%', (205, 205, 50))
        self.ammoIndicator.textedit(f'Ammo: {player.weapon.ammo if player.weapon != None else 0}/{player.weapon.maxammo if player.weapon != None else 0}/{player.weapon.ammunition if player.weapon != None else 0}', (50, 205, 50))

        self.ammunitionIndicator.textedit(f'Ammunition', (50, 205, 50))
        self.assaultRiffleAmmunitionIndicator.textedit(f'Assault Rifle ammunition: {player.inventory.get("assaultRiffleAmmunition", 0)}', (50, 205, 50))
        self.shotgunAmmunitionIndicator.textedit(f'Shotgun ammunition: {player.inventory.get("shotgunAmmunition", 0)}', (50, 205, 50))
        self.pistolAmmunitionIndicator.textedit(f'Pistol ammunition: {player.inventory.get("pistolAmmunition", 0)}', (50, 205, 50))

    def pausescreen(self, paused):
        if paused:
            self.shadeground.hided = False
            self.pauselabel.hided = False
        else:
            self.shadeground.hided = True
            self.pauselabel.hided = True

    def update(self, paused, player):
        self.cursorrender()
        self.indicators(player)
        self.pausescreen(paused)