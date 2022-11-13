import math
import pygame

def distanceСalculation(first, second):
    distancex = first.rect.x - second.rect.x
    distancey = first.rect.y - second.rect.y
    distance = math.sqrt(distancex **2 + distancey**2)
    return distance