
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

    def update(self, entity_group, screen, mouse, dtime, TARGET_FPS):
        self.healthbar(screen)
    
    def __del__(self):
        self.kill()

class Bullet(Entity):
    _instances = set()

    def __init__(self, vector, player, entitygroup=None, selfentitygroup=None):
        Bullet._instances.add(self)
        Entity._instances.add(self)
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.center = player.rect.center
        if entitygroup != None:
            self.add(entitygroup)
        if selfentitygroup !=None:
            self.add(selfentitygroup)
        self.firstplace = player.rect.center
        self.speedx = 0
        self.speedy = 0
        self.vector = vector
        self.range = 600
        self.damage = 40

    def movement(self, entitygroup, dtime, TARGET_FPS):
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

        self.goal(entitygroup, distancecurrent, distancestart)

    def goal(self, entitygroup, distancecurrent, distancestart):
        hit = pygame.sprite.spritecollideany(self, entitygroup)
        if hit:
            hit.health -= self.damage
            self.__del__()
        elif distancecurrent == 0 or (distancestart - distancecurrent >= self.range):
            self.__del__()

    def update(self, entitygroup, screen, mouse, dtime, TARGET_FPS):
        self.movement(entitygroup, dtime, TARGET_FPS)

    def __del__(self):
        self.kill()

class Player(Entity):
    _instances = set()

    def __init__(self, color, resolution, keys, name='Player', entitygroup=None, textentitygroup=None, selfentitygroup=None):
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
        if selfentitygroup !=None:
            self.add(selfentitygroup)
        self.name = modules.mysprites.Text(name, 24, entity=self, textentitygroup=textentitygroup)
        self.health = 100
        self.maxhealth = 100

        self.K_moveup = keys[0]
        self.K_moveleft = keys[1]
        self.K_movedown = keys[2]
        self.K_moveright = keys[3]

    def movement(self, dtime, TARGET_FPS):
        keystate = pygame.key.get_pressed()
        v = math.sqrt(self.speedx**2 + self.speedy**2)
        kx = abs((self.speedx / v) if self.speedx != 0 else 1)
        ky = abs((self.speedy / v) if self.speedy != 0 else 1)

        if keystate[self.K_moveup]:
            self.speedy = -6 * ky
        if keystate[self.K_movedown]:
            self.speedy = 6 * ky
        if keystate[self.K_moveleft]:
            self.speedx = -6 * kx
        if keystate[self.K_moveright]:
            self.speedx = 6 * kx

        if (not keystate[self.K_moveup]) and (not keystate[self.K_movedown]):
            self.speedy += 1 if self.speedy < 0 else 0
            self.speedy -= 1 if self.speedy > 0 else 0

        if (not keystate[self.K_moveleft]) and (not keystate[self.K_moveright]):
            self.speedx += 1 if self.speedx < 0 else 0
            self.speedx -= 1 if self.speedx > 0 else 0

        self.speedx = math.ceil(self.speedx) if self.speedx > 0 else math.floor(self.speedx)
        self.speedy = math.ceil(self.speedy) if self.speedy > 0 else math.floor(self.speedy)

        self.rect.x += self.speedx * dtime * TARGET_FPS
        self.rect.y += self.speedy * dtime * TARGET_FPS

    def borders(self):
        if self.rect.right > self.resolution[0]: self.rect.right = self.resolution[0]
        if self.rect.left < 0: self.rect.left = 0
        if self.rect.bottom > self.resolution[1]: self.rect.bottom = self.resolution[1]
        if self.rect.top < 0: self.rect.top = 0

    def attack(self, screen, mouse):
        mousestate = pygame.mouse.get_pressed()

    def update(self, entity_group, screen, mouse, dtime, TARGET_FPS):
        self.movement(dtime, TARGET_FPS)
        self.borders()
        self.attack(screen, mouse)
        self.healthbar(screen)

    def __del__(self):
        self.kill()
        self.name.kill()

class Zombie(Entity):
    _instances = set()

    def __init__(self, name='Zombie', target=None, entitygroup=None, textentitygroup=None, selfentitygroup=None):
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
        self.name = modules.mysprites.Text(name, 24, entity=self, textentitygroup=textentitygroup)
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
            self.speedx = (5 if abs(dx) >= 5 else 1) * kx
            self.speedy = (5 if abs(dy) >= 5 else 1) * ky
            self.speedx = math.ceil(self.speedx) if self.speedx > 0 else math.floor(self.speedx)
            self.speedy = math.ceil(self.speedy) if self.speedy > 0 else math.floor(self.speedy)
        else:
            self.speedx, self.speedy = 0, 0
        self.rect.x += self.speedx * dtime * TARGET_FPS
        self.rect.y += self.speedy * dtime * TARGET_FPS

    def update(self, entity_group, screen, mouse, dtime, TARGET_FPS):
        self.movement(dtime, TARGET_FPS)
        self.healthbar(screen)

    def __del__(self):
        self.kill()
        if self.name:
            self.name.kill()

class Text(pygame.sprite.Sprite):
    _instances = set()

    def __init__(self, text, size, color = (0, 0, 0), alone=False, position=(0, 0), entity=None, textentitygroup=None):
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