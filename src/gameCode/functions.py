import math
import pygame
import copy

def distanceСalculation(first, second):
    distancex = first.rect.x - second.rect.x
    distancey = first.rect.y - second.rect.y
    distance = math.sqrt(distancex **2 + distancey**2)
    return distance

def founditem(storage, item):
    for key, value in storage.items():
        if value and item:
            if (value.firstItemType == item.firstItemType) and (value.secondItemType == item.secondItemType) and (value.itemName == item.itemName):
                return key, value
        elif (value == None) and (item == None):
            return key, value
    else:
        return None, None

def founditems(storage, item):
    itemsstorage = dict()
    for key, value in storage.items():
        if value and item:
            if (value.firstItemType == item.firstItemType) and (value.secondItemType == item.secondItemType) and (value.itemName == item.itemName):
                itemsstorage[key] = value
        elif (value == None) and (item == None):
            itemsstorage[key] = value
    return itemsstorage

def checkEquivalence(firstitem, seconditem):
    if firstitem and seconditem:
        if firstitem.firstItemType == seconditem.firstItemType:
            if firstitem.secondItemType == seconditem.secondItemType:
                if firstitem.itemName == seconditem.itemName:
                    return True
    elif not firstitem and seconditem:
        return True
    return False

def createItem(item=None, amountValue=1):
    item = copy.deepcopy(item)
    item.amountValue = amountValue
    return item

def pressButton(func):
    def wrapper(button, buttonState, buttonSwitch):
        if buttonState == True:
            if not buttonSwitch[button]:
                buttonSwitch[button] = True
                func()
        else:
            buttonSwitch[button] = False
    return wrapper

