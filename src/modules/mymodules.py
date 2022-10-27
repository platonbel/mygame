import pygame
import random
import modules


def checkSpriteCollision(sprites):
    for curSprite in sprites:
        collidedSprites = pygame.sprite.groupcollide(sprites, sprites, True, True)

def cursor(screen, mouse):
    mousex, mousey = mouse
    crosshair_image = pygame.Surface((10, 10))
    crosshair_image.fill((75, 0, 0))
    crosshair_image_rect = crosshair_image.get_rect()
    crosshair_image_rect.center = (mousex, mousey)
    screen.blit(crosshair_image, crosshair_image_rect)

def zombieSpawn(entitygroup_zombie, entitygroup_player, textentitygroup, entitygroup):
    zombie = modules.mysprites.Zombie(name='Zombie', target=random.choice(entitygroup_player.sprites()), entitygroup=entitygroup, textentitygroup=textentitygroup, selfentitygroup=entitygroup_zombie)
    return zombie

