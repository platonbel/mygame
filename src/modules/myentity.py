
import pygame
import modules
import random
import math

class Entity(pygame.sprite.Sprite):
    _instances = set()

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.speedx = 0
        self.speedy = 0
        self.health = math.inf
        self.maxhealth = math.inf
        
    def collision(self):
        None

    def healthbar(self, screen):
        if self.health <= 0:
            self.health = 0
            self.__del__()
        if self.maxhealth == math.inf:
            healthratio = 1
        else:
            healthratio = self.health / self.maxhealth

        bar_lenght = 100 
        bar_height = 10

        bar_outline_image = pygame.Surface((bar_lenght, bar_height))
        bar_outline_image.fill((192, 192, 192))
        bar_outline_image_rect = bar_outline_image.get_rect()
        bar_outline_image_rect.center = (self.rect.center[0], self.rect.center[1]+30)

        bar_image = pygame.Surface((round(bar_lenght*healthratio), bar_height))
        bar_image.fill((0, 255, 0))
        bar_image_rect = bar_outline_image.get_rect()
        bar_image_rect.center = (self.rect.center[0], self.rect.center[1]+30)

        screen.blit(bar_outline_image, bar_outline_image_rect)
        screen.blit(bar_image, bar_image_rect)

    def update(self, screen, mouse, dtime, TARGET_FPS):
        self.healthbar(screen)
    
    def __del__(self):
        self.kill()

class Bullet(Entity):
    _instances = set()

    def __init__(self, vector, player, damage=40, range=600, entitygroup=None, selfenemygroup=None):
        Bullet._instances.add(self)
        Entity._instances.add(self)
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = player.rect.center
        self.firstplace = player.rect.center
        if entitygroup != None:
            self.add(entitygroup)
        self.targets = selfenemygroup
        self.vector = vector
        self.range = range
        self.damage = damage
        self.speedx = 0
        self.speedy = 0

    def movement(self, dtime, TARGET_FPS):
        dx = self.vector[0] - self.rect.center[0]
        dy = self.vector[1] - self.rect.center[1]
        distancecurrent = math.sqrt(dx**2 + dy**2)

        dx1 = self.vector[0] - self.firstplace[0]
        dy1 = self.vector[1] - self.firstplace[1]
        distancestart = math.sqrt(dx1**2 + dy1**2)

        kx = (dx / distancecurrent) if distancecurrent != 0 else 0
        ky = (dy / distancecurrent) if distancecurrent != 0 else 0
        self.speedx = (20 if abs(dx) >= 20 else 1) * kx
        self.speedy = (20 if abs(dy) >= 20 else 1) * ky
        self.speedx = math.ceil(self.speedx) if self.speedx > 0 else math.floor(self.speedx)
        self.speedy = math.ceil(self.speedy) if self.speedy > 0 else math.floor(self.speedy)
        
        self.rect.x += self.speedx * dtime * TARGET_FPS
        self.rect.y += self.speedy * dtime * TARGET_FPS

        self.goal(distancecurrent, distancestart)

    def goal(self, distancecurrent, distancestart):
        hit = pygame.sprite.spritecollideany(self, self.targets)
        if hit:
            hit.health -= self.damage

            self.__del__()
        elif distancecurrent == 0 or (distancestart - distancecurrent >= self.range):
            self.__del__()

    def update(self, screen, mouse, mousestate, keystate, entitygroup, dtime, TARGET_FPS):
        self.movement(dtime, TARGET_FPS)

    def __del__(self):
        self.kill()

class Player(Entity):
    _instances = set()

    def __init__(self, color, resolution, name='Player', entitygroup=None, selfentitygroup=None, selfenemygroup=None, textentitygroup=None):
        Player._instances.add(self)
        Entity._instances.add(self)
        super().__init__()

        self.resolution = resolution
        self.image = pygame.Surface((40, 40))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (self.resolution[0] / 2 + random.randint(1, 256), self.resolution[1] / 2 + random.randint(1, 256))
        if entitygroup != None:
            self.add(entitygroup)
        if selfentitygroup != None:
            self.add(selfentitygroup)

        self.weapon = Weapon(self, selfenemygroup) 
        self.name = modules.myentity.Text(name, 24, entity=self, textentitygroup=textentitygroup)
        self.health = 100
        self.maxhealth = 100
        self.energy = 100
        self.maxenergy = 100
        self.keyswith = {'K_LSHIFT': True}

    def movement(self, keystate, dtime, TARGET_FPS):
        v = math.sqrt(self.speedx**2 + self.speedy**2)
        kx = abs((self.speedx / v) if self.speedx != 0 else 1)
        ky = abs((self.speedy / v) if self.speedy != 0 else 1)

        if keystate[pygame.K_LSHIFT] and self.energy != 0 and self.keyswith['K_LSHIFT']:
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

        if keystate[pygame.K_w]:
            self.speedy = -6 * ky * sprint
        if keystate[pygame.K_s]:
            self.speedy = 6 * ky * sprint
        if keystate[pygame.K_a]:
            self.speedx = -6 * kx * sprint
        if keystate[pygame.K_d]:
            self.speedx = 6 * kx * sprint

        if (not keystate[pygame.K_w]) and (not keystate[pygame.K_s]):
            self.speedy += 1 if self.speedy < 0 else 0
            self.speedy -= 1 if self.speedy > 0 else 0

        if (not keystate[pygame.K_a]) and (not keystate[pygame.K_d]):
            self.speedx += 1 if self.speedx < 0 else 0
            self.speedx -= 1 if self.speedx > 0 else 0

        self.speedx = math.ceil(self.speedx) if self.speedx > 0 else math.floor(self.speedx)
        self.speedy = math.ceil(self.speedy) if self.speedy > 0 else math.floor(self.speedy)

        self.rect.x += self.speedx * dtime * TARGET_FPS
        self.rect.y += self.speedy * dtime * TARGET_FPS

    def energybar(self, screen):
        energyratio = self.energy / self.maxenergy
        bar_lenght = 100 
        bar_height = 10

        bar_outline_image = pygame.Surface((bar_lenght, bar_height))
        bar_outline_image.fill((192, 192, 192))
        bar_outline_image_rect = bar_outline_image.get_rect()
        bar_outline_image_rect.center = (self.rect.center[0], self.rect.center[1]+45)

        bar_image = pygame.Surface((round(bar_lenght*energyratio), bar_height))
        bar_image.fill((255, 255, 0))
        bar_image_rect = bar_outline_image.get_rect()
        bar_image_rect.center = (self.rect.center[0], self.rect.center[1]+45)

        screen.blit(bar_outline_image, bar_outline_image_rect)
        screen.blit(bar_image, bar_image_rect)

    def borders(self):
        if self.rect.right > self.resolution[0]: self.rect.right = self.resolution[0]
        if self.rect.left < 0: self.rect.left = 0
        if self.rect.bottom > self.resolution[1]: self.rect.bottom = self.resolution[1]
        if self.rect.top < 0: self.rect.top = 0

    def curWeapon(self, mouse, mousestate, keystate, entitygroup):
        self.weapon.attack(mouse, mousestate, entitygroup)
        self.weapon.reload(keystate)

    def update(self, screen, mouse, mousestate, keystate, entitygroup, dtime, TARGET_FPS):
        self.movement(keystate, dtime, TARGET_FPS)
        self.curWeapon(mouse, mousestate, keystate, entitygroup)
        self.borders()
        self.healthbar(screen)
        self.energybar(screen)

    def __del__(self):
        self.kill()
        self.name.kill()

class Zombie(Entity):
    _instances = set()

    def __init__(self, name='Zombie', target=None, entitygroup=None, selfentitygroup=None, textentitygroup=None):
        Zombie._instances.add(self)
        Entity._instances.add(self)
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((75, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (360, 360)
        if entitygroup != None:
            self.add(entitygroup)
        if selfentitygroup !=None:
            self.add(selfentitygroup)
        self.name = modules.myentity.Text(name, 24, entity=self, textentitygroup=textentitygroup)
        self.health = 200
        self.maxhealth = 200
        self.target = target

    def movement(self, dtime, TARGET_FPS):
        if self.target:
            dx = self.target.rect.x - self.rect.x
            dy = self.target.rect.y - self.rect.y
            v = math.sqrt(dx**2 + dy**2)
            kx = (dx / v) if v != 0 else 0
            ky = (dy / v) if v != 0 else 0
            self.speedx = (6 if abs(dx) >= 6 else 1) * kx
            self.speedy = (6 if abs(dy) >= 6 else 1) * ky
            self.speedx = math.ceil(self.speedx) if self.speedx > 0 else math.floor(self.speedx)
            self.speedy = math.ceil(self.speedy) if self.speedy > 0 else math.floor(self.speedy)
        else:
            self.speedx, self.speedy = 0, 0
        self.rect.x += self.speedx * dtime * TARGET_FPS
        self.rect.y += self.speedy * dtime * TARGET_FPS

    def attack(self, screen):   
        None

    def update(self, screen, mouse, mousestate, keystate, entitygroup, dtime, TARGET_FPS):
        self.movement(dtime, TARGET_FPS)
        self.healthbar(screen)

    def __del__(self):
        self.kill()
        if self.name:
            self.name.kill()

class Text(pygame.sprite.Sprite):
    _instances = set()

    def __init__(self, text='text', size=24, color = (0, 0, 0), position=(0, 0), alone=False, entity=None, textentitygroup=None):
        if alone == False:
            Text._instances.add(self)
        super().__init__()
        self.font = pygame.font.SysFont('arial', size)
        self.image = self.font.render(text, True, color)
        self.rect = self.image.get_rect()
        self.rect.center = position
        if textentitygroup != None:
            self.add(textentitygroup)
        self.entity = entity

    def moving(self):
        if self.entity:
            self.rect.center = (self.entity.rect.center[0], self.entity.rect.center[1]-self.entity.image.get_height())

    def update(self):
        self.moving()

    def __del__(self):
        self.kill()

class Weapon():
    def __init__(self, shooter, selfenemygroup):
        self.damage = 40
        self.range = 600
        self.ammo = 17
        self.maxammo = 17
        self.ammunition = math.inf
        self.shooter = shooter
        self.targets = selfenemygroup
        self.keyswith = {'K_r': True}
        self.mouseswith = {'0': True}

    def attack(self, mouse, mousestate, entitygroup):
        if mousestate[0] and self.ammo != 0:
            if self.mouseswith['0']:
                self.ammo -= 1
                modules.mymodules.bulletSpawn(mouse=mouse, shooter=self.shooter, damage=self.damage, range=self.range, entitygroup=entitygroup, selfenemygroup=self.targets)
            self.mouseswith['0'] = False
        else:
            self.mouseswith['0'] = True

    def reload(self, keystate):
        if keystate[pygame.K_r]:
            if self.keyswith['K_r']:
                totalammo = self.ammunition + self.ammo
                self.ammo = min(totalammo, self.maxammo)
                self.ammunition = totalammo - self.ammo
            self.keyswith['K_r'] = False
        else:
            self.keyswith['K_r'] = True
    
