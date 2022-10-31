
import pygame
import math
from modules import classmodules, gameentity, gametext

class Player(gameentity.defaultentity.Entity):
    instances = set()

    def __init__(self, position=(0, 0), image=None, name=None, layer=0):
        Player.instances.add(self)
        super().__init__()
        self.add(gameentity.entitygroup.playergroup)
        gameentity.entitylayer.defaultlayer.add(self, layer=layer)

        #realize here import png sprites
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 200, 255))
        self.rect = self.image.get_rect()

        #render options
        self.hided = False
        self._layer = layer

        #realize here import spawnpoint info 
        self.rect.center = position

        #characteristics
        self.health = 100
        self.maxhealth = 100
        self.energy = 100
        self.maxenergy = 100

        #name binding
        self.name = gametext.defaulttext.Text(name, side='center', position=(position[0], position[1]-30))

        #weapon binding
        self.weapon = classmodules.Weapon(self, gameentity.entitygroup.zombiegroup)

        #const of put/unput buttons
        self.keyswith = {'K_LSHIFT': False, 'K_w': False, 'K_a': False, 'K_s': False, 'K_d': False}
        self.mouseswith = {'0': False, '1': False, '2': False}

    def movement(self, keystate, dtime, TARGET_FPS):
        #set the movement vector
        movementvector = math.sqrt(self.speedx**2 + self.speedy**2)
        kxvector = abs((self.speedx / movementvector) if self.speedx != 0 else 1)
        kyvector = abs((self.speedy / movementvector) if self.speedy != 0 else 1)

        #checking for sprint
        if keystate[pygame.K_LSHIFT] and self.energy != 0 and ((self.speedx != 0) or (self.speedy != 0)) and self.keyswith['K_LSHIFT']:
            sprint = 1.3
            self.energy = (self.energy - 15 * dtime) if self.energy > 0 else 0
            if self.energy == 0:
                sprint = 1
                self.keyswith['K_LSHIFT'] = False
        else:
            sprint = 1
            self.energy = (self.energy + 15 * dtime) if self.energy < 100 else 100
            if not keystate[pygame.K_LSHIFT]:
                self.keyswith['K_LSHIFT'] = True

        #moving
        if keystate[pygame.K_w]:
            self.speedy = -6 * kyvector * sprint
        if keystate[pygame.K_a]:
            self.speedx = -6 * kxvector * sprint
        if keystate[pygame.K_s]:
            self.speedy = 6 * kyvector * sprint
        if keystate[pygame.K_d]:
            self.speedx = 6 * kxvector * sprint

        #stopping if no press
        if (not keystate[pygame.K_w]) and (not keystate[pygame.K_s]):
            self.speedy += 1 if self.speedy < 0 else 0
            self.speedy -= 1 if self.speedy > 0 else 0

        if (not keystate[pygame.K_a]) and (not keystate[pygame.K_d]):
            self.speedx += 1 if self.speedx < 0 else 0
            self.speedx -= 1 if self.speedx > 0 else 0

        #set the speed and updating the sprite position
        self.speedx = math.ceil(self.speedx) if self.speedx > 0 else math.floor(self.speedx)
        self.speedy = math.ceil(self.speedy) if self.speedy > 0 else math.floor(self.speedy)

        self.rect.x += self.speedx * dtime * TARGET_FPS
        self.rect.y += self.speedy * dtime * TARGET_FPS

    def namerender(self):
        #giving to connected text label the position
        self.name.position = (self.rect.center[0], self.rect.center[1]-40)

    def visible(self):
        #displaying the sprite if not hided
        if self.hided:
            self.image.set_alpha(0)
        else:
            self.image.set_alpha(255)

    def currentWeapon(self, mouse, mousestate, keystate):
        self.weapon.attack(mouse, mousestate)
        self.weapon.reload(keystate)

    def update(self, mouse, mousestate, keystate, screen, dtime, TARGET_FPS):
        self.movement(keystate, dtime, TARGET_FPS)
        self.currentWeapon(mouse, mousestate, keystate)
        self.borders(screen)
        self.namerender()
        self.visible()

    def __del__(self):
        self.kill()
        self.name.kill()