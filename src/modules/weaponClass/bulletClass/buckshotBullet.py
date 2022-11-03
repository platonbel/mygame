from this import d
import pygame
import math
import random
from modules.weaponClass import bulletClass


def Buckshot(shooter, targets, mouse, spreadangle, shotrange, damage, amount=8):
    for i in range(amount):
        bulletClass.defaultBullet.Bullet(shooter=shooter, targets=targets, mouse=mouse, spreadangle=spreadangle, shotrange=shotrange, damage=damage)
