
import pygame
import random
import modules


def checkSpriteCollision(sprites):
    for curSprite in sprites:
        collidedSprites = pygame.sprite.groupcollide(sprites, sprites, True, True)

def cursor(screen, mouse):
    crosshair_image = pygame.Surface((10, 10))
    crosshair_image.fill((75, 0, 0))
    crosshair_image_rect = crosshair_image.get_rect()
    crosshair_image_rect.center = mouse
    screen.blit(crosshair_image, crosshair_image_rect)

def zombieSpawn(entitygroup_zombie, entitygroup_player, textentitygroup, entitygroup, layerentityupdates):
    zombie = modules.myentity.Zombie(name='Zombie', target=random.choice(entitygroup_player.sprites()), entitygroup=entitygroup, selftextentitygroup=textentitygroup, selfentitygroup=entitygroup_zombie, layerentityupdates=layerentityupdates)

def bulletSpawn(mouse, shooter, damage, range, entitygroup, selfenemygroup, layerentityupdates):
    modules.myentity.Bullet(vector=mouse, player=shooter, damage=damage, range=range, entitygroup=entitygroup, selfenemygroup=selfenemygroup, layerentityupdates=layerentityupdates)
