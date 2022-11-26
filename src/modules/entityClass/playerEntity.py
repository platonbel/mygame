
import pygame
import math
import copy
from modules import entityClass, textClass, itemClass, shapeClass, interfaceClass, inventoryClass, effectsClass

class Player(entityClass.defaultEntity.Entity):
    instances = set()

    def __init__(self, position=(0, 0), image=None, name=None, interface=None, layer=0):
        Player.instances.add(self)
        super().__init__()
        self.add(entityClass.instances.entityGroup.playerGroup)
        entityClass.instances.entityLayer.defaultLayer.add(self, layer=layer)

        #realize here import png sprites
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 200, 255))
        self.rect = self.image.get_rect()

        #render options
        self.hided = False

        #realize here import spawnpoint info
        self.position = (0, 0)
        self.rect.center = self.position

        #characteristics
        self.health = 100
        self.maxhealth = 100
        self.stamina = 100
        self.maxstamina = 100
        self.speed = 6

        #targets binding
        self.enemygroup = entityClass.instances.entityGroup.zombieGroup

        #gui binding
        self.name = textClass.defaultText.Text(text=name, side='center', position=(position[0], position[1]-30))
        self.healthbarback = shapeClass.defaultShape.Shape(size=(100, 8), side='center', color=(192, 192, 192))
        self.healthbar = shapeClass.defaultShape.Shape(size=(100, 8), side='center', color=(0, 255, 0))

        #game interaction

        self.inventory = inventoryClass.defaultInventory.Inventory()
        self.effects = effectsClass.defaultEffects.Effects(self)

        self.inventory.inventoryslots['9'] = copy.deepcopy(itemClass.instances.rangedWeaponGroup.items['AK-47'])
        self.inventory.inventoryslots['13'] = copy.deepcopy(itemClass.instances.rangedWeaponGroup.items['AK-47'])
        self.inventory.inventoryslots['14'] = copy.deepcopy(itemClass.instances.ammunitionGroup.items['7.62'])
        self.inventory.inventoryslots['14'].amount = 500
        self.inventory.inventoryslots['12'] = copy.deepcopy(itemClass.instances.ammunitionGroup.items['12/70'])
        self.inventory.inventoryslots['12'].amount = 500
        self.inventory.inventoryslots['10'] = copy.deepcopy(itemClass.instances.suppliesGroup.items['First Aid Kit'])
        self.inventory.inventoryslots['10'].amount = 228
        self.inventory.inventoryslots['11'] = copy.deepcopy(itemClass.instances.suppliesGroup.items['damager'])
        self.inventory.inventoryslots['11'].amount = 1337
        self.inventory.inventoryslots['1'] = copy.deepcopy(itemClass.instances.rangedWeaponGroup.items['testgun'])
        self.inventory.inventoryslots['2'] = copy.deepcopy(itemClass.instances.rangedWeaponGroup.items['SPAS-12'])
        self.inventory.inventoryslots['3'] = copy.deepcopy(itemClass.instances.rangedWeaponGroup.items['Glock-17'])
        self.inventory.inventoryslots['4'] = copy.deepcopy(itemClass.instances.rangedWeaponGroup.items['AK-47'])

        #const of put/unput buttons
        self.keyswith = {'K_LSHIFT': False, 'K_0': False, 'K_1': False, 'K_2': False, 'K_3': False, 'K_w': False, 'K_a': False, 'K_s': False, 'K_d': False}
        self.mouseswith = {'0': False, '1': False, '2': False}

    def movement(self, keystate, dtime, TARGET_FPS):
        #set the movement vector
        movementvector = math.sqrt(self.speedx**2 + self.speedy**2)
        kxvector = abs((self.speedx / movementvector) if self.speedx != 0 else 1)
        kyvector = abs((self.speedy / movementvector) if self.speedy != 0 else 1)

        #checking for sprint
        if keystate[pygame.K_LSHIFT] and self.stamina != 0 and ((self.speedx != 0) or (self.speedy != 0)) and self.keyswith['K_LSHIFT']:
            sprint = 1.3
            self.stamina = (self.stamina - 15 * dtime) if self.stamina > 0 else 0
            if self.stamina == 0:
                sprint = 1
                self.keyswith['K_LSHIFT'] = False
        else:
            sprint = 1
            self.stamina = (self.stamina + 15 * dtime) if self.stamina < 100 else 100
            if not keystate[pygame.K_LSHIFT]:
                self.keyswith['K_LSHIFT'] = True

        if self.stamina > self.maxstamina:
            self.stamina = self.maxstamina

        #moving
        if keystate[pygame.K_w]:
            self.speedy = -self.speed * kyvector * sprint
        if keystate[pygame.K_a]:
            self.speedx = -self.speed * kxvector * sprint
        if keystate[pygame.K_s]:
            self.speedy = self.speed * kyvector * sprint
        if keystate[pygame.K_d]:
            self.speedx = self.speed * kxvector * sprint

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

        self.rect.centerx += self.speedx * dtime * TARGET_FPS
        self.rect.centery += self.speedy * dtime * TARGET_FPS

    def GUIRender(self):
        healthratio = self.health / self.maxhealth
        self.healthbar.sizeedit((round(100*healthratio), 8))
        self.healthbar.rect = self.healthbarback.image.get_rect()

        self.name.moving((self.rect.center[0], self.rect.center[1]-40))
        self.healthbarback.moving((self.rect.center[0], self.rect.center[1]+30))
        self.healthbar.moving((self.rect.center[0], self.rect.center[1]+30))

    def visible(self, hided):
        self.hided = hided
        if self.hided:
            self.image.set_alpha(0)
        else:
            self.image.set_alpha(255)

    def inventoryUpdate(self, mouse, mousestate, keystate, dtime, TARGET_FPS):
        self.inventory.inventoryRender(keystate)
        self.inventory.quickAccesBarRender(self, mouse, mousestate, keystate, dtime, TARGET_FPS)
            
    def statiscticsUpdate(self, dtime, TARGET_FPS):
        self.effects.update(dtime, TARGET_FPS)
        if self.health <= 0:
            self.health = 0
            self.__del__()
        elif self.health > self.maxhealth:
            self.health = self.maxhealth
        if self.stamina <= 0:
            self.stamina = 0
        elif self.stamina > self.maxstamina:
            self.stamina = self.maxstamina

    def update(self, mouse, mousestate, keystate, screen, dtime, TARGET_FPS):
        self.movement(keystate, dtime, TARGET_FPS)
        self.inventoryUpdate(mouse, mousestate, keystate, dtime, TARGET_FPS)
        self.statiscticsUpdate(dtime, TARGET_FPS)
        self.borders(screen)
        self.GUIRender()

    def __del__(self):
        self.kill()
        self.name.kill()
        self.healthbar.kill()
        self.healthbarback.kill()