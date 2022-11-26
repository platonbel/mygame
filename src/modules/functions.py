import math
import pygame

def distanceСalculation(first, second):
    distancex = first.rect.x - second.rect.x
    distancey = first.rect.y - second.rect.y
    distance = math.sqrt(distancex **2 + distancey**2)
    return distance

def founditem(storage, item):
    for key, value in storage.items():
        if value and item:
            if value.itemtype == item.itemtype:
                match value.itemtype:
                    case 'ammunition':
                        if value.ammunitiontype == item.ammunitiontype:
                            if value.itemname == item.itemname:
                                return key, value
                    case 'rangedWeapon':
                        if value.weapontype == item.weapontype:
                            if value.itemname == item.itemname:
                                return key, value
                    case 'supplies':
                        if value.suppliestype == item.suppliestype:
                            if value.itemname == item.itemname:
                                return key, value
        elif (value == None) and (item == None):
            return key, value
    else:
        return None, None

def founditems(storage, item):
    itemsstorage = dict()
    for key, value in storage.items():
        if value and item:
            if value.itemtype == item.itemtype:
                match value.itemtype:
                    case 'ammunition':
                        if value.ammunitiontype == item.ammunitiontype:
                            if value.itemname == item.itemname:
                                itemsstorage[key] = value
                    case 'rangedWeapon':
                        if value.weapontype == item.weapontype:
                            if value.itemname == item.itemname:
                                itemsstorage[key] = value
                    case 'supplies':
                        if value.suppliestype == item.suppliestype:
                            if value.itemname == item.itemname:
                                itemsstorage[key] = value
        elif (value == None) and (item == None):
            itemsstorage[key] = value
    return itemsstorage

def checkEquivalence(firstitem, seconditem):
    if firstitem and seconditem:
        if firstitem.itemtype == seconditem.itemtype:
            match firstitem.itemtype:
                case 'ammunition':
                    if firstitem.ammunitiontype == seconditem.ammunitiontype:
                        if firstitem.itemname == seconditem.itemname:
                            return True
                case 'rangedWeapon':
                    if firstitem.weapontype == seconditem.weapontype:
                        if firstitem.itemname == seconditem.itemname:
                            return True
                case 'supplies':
                    if firstitem.suppliestype == seconditem.suppliestype:
                        if firstitem.itemname == seconditem.itemname:
                            return True
    elif not firstitem and seconditem:
        return True
    return False

