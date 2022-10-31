import pygame
import math
from modules import gameentity, gametext, gameshape, privategameobject

class Weapon():
    
    def __init__(self, shooter, enemygroup):
        self.damage = 40
        self.range = 600
        self.ammo = math.inf
        self.maxammo = math.inf
        self.ammunition = math.inf
        self.shooter = shooter
        self.targets = enemygroup
        self.keyswith = {'K_r': False}
        self.mouseswith = {'0': False}

    def attack(self, mouse, mousestate):
        if mousestate[0] and self.ammo != 0:
            if self.mouseswith['0']:
                self.ammo -= 1
                gameentity.bulletentity.Bullet(self.shooter, self.targets, mouse, range=self.range, damage=self.damage)
                self.mouseswith['0'] = False
        else:
            self.mouseswith['0'] = True

    def reload(self, keystate):
        if keystate[pygame.K_r]:
            if self.keyswith['K_r']:
                totalammo = self.ammunition + self.ammo
                self.ammo = min(totalammo, self.maxammo)
                self.ammunition = totalammo - self.ammo
            self.keyswith['K_r'] = True
        else:
            self.keyswith['K_r'] = False

class Interface():

    def __init__(self, screen):
        self.healthindicator = gametext.defaulttext.Text(position=(screen.get_width()-60, screen.get_height()-120), side='bottomright', layer=0, private=privategameobject.privateobjectlayer.interfacelayer)
        self.staminaindicator = gametext.defaulttext.Text(position=(screen.get_width()-60, screen.get_height()-90), side='bottomright', layer=0, private=privategameobject.privateobjectlayer.interfacelayer)
        self.ammoindicator = gametext.defaulttext.Text(position=(screen.get_width()-60, screen.get_height()-60), side='bottomright', layer=0, private=privategameobject.privateobjectlayer.interfacelayer)

        self.pauselabel = gametext.defaulttext.Text(text='PAUSE', size=72, position=(screen.get_width()//2, screen.get_height()//2), side='center', layer=1, private=privategameobject.privateobjectlayer.interfacelayer)

        self.shadeground = gameshape.defaultshape.Shape(size=screen.get_size(), position=(0, 0), side='topleft', color=(0, 0, 0), alpha=75, layer=2, private=privategameobject.privateobjectlayer.interfacelayer)

    def indicators(self, player):
        self.healthindicator.textedit(f'Health: {round((player.health/player.maxhealth if player.maxhealth != math.inf else 1)*100)}%', (255, 100, 100))
        self.staminaindicator.textedit(f'Stamina: {round((player.energy/player.maxenergy if player.maxenergy != math.inf else 1)*100)}%', (255, 255, 100))
        self.ammoindicator.textedit(f'Ammo: {player.weapon.ammo}/{player.weapon.maxammo}/{player.weapon.ammunition}', (100, 255, 100))
    
    def pausescreen(self, screen, paused):
        if paused:
            self.shadeground.hided = False
            self.pauselabel.hided = False
        else:
            self.shadeground.hided = True
            self.pauselabel.hided = True

    def update(self, screen, paused, player):
        self.indicators(player)
        self.pausescreen(screen, paused)