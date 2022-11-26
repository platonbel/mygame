import pygame
import math
from modules import entityClass, interfaceClass, textClass, shapeClass, functions

class Indicator():

    def __init__(self, screen):
        self.hided = True
        
        self.itemIndicator = shapeClass.privateShape.Shape(image="src/assets/textures/item_indicator.png", position=(screen.get_width()-30, screen.get_height()-142), side='bottomright', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.pickingBarIndicator = shapeClass.privateShape.Shape(image="src/assets/textures/picking_item_indicator.png", headobject=self.itemIndicator, side='topleft', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.usingBarIndicator = shapeClass.privateShape.Shape(image="src/assets/textures/using_item_indicator.png", headobject=self.itemIndicator, side='bottomleft', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)

        self.pickingbar = shapeClass.privateShape.Shape(headobject=self.pickingBarIndicator, size=(384, 12), side='topleft', color=(96, 55, 217), layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.usingbar = shapeClass.privateShape.Shape(headobject=self.usingBarIndicator, size=(384, 12), side='topleft', color=(217, 55, 96), layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)

        self.ammovalue = textClass.privateText.Text(headobject=self.itemIndicator, size=36, side='center', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.ammunitionvalue = textClass.privateText.Text(headobject=self.itemIndicator, size=36, side='center', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)
        self.ammunitiontypevalue = textClass.privateText.Text(headobject=self.itemIndicator, size=36, side='center', layer=3, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)

        self.itemicon = shapeClass.privateShape.Shape(image="src/assets/textures/default_icon.png", headobject=self.itemIndicator, side='center', layer=2, privateLayer=interfaceClass.instances.interfaceLayer.defaultLayer)

    def indicatorrender(self, screen, player):
        if player:
            if player.inventory.item:

                match player.inventory.item.itemtype:
                    case 'rangedWeapon':
                        ammoratio = player.inventory.item.ammo
                        maxammoratio = player.inventory.item.maxammo
                        aviableammunition = functions.founditems(player.inventory.inventoryslots, player.inventory.item.ammunition)
                        ammunitionratio = sum([value.amount for value in aviableammunition.values()]) if aviableammunition else 0
                        ammunitiontyperatio = player.inventory.item.ammunitiontype + ' к.'
                        itemiconlink = player.inventory.item.itemicon
                        self.itemIndicator.visible(False)

                        if not player.inventory.item.picked:
                            pickingratio = player.inventory.item.pickingdelay / player.inventory.item.pickingtime if player.inventory.item.pickingtime else 0
                            self.itemIndicator.moving((screen.get_width()-30, screen.get_height()-186))
                            self.pickingBarIndicator.visible(False)
                            self.pickingbar.visible(False)
                        else:
                            pickingratio = 0
                            self.itemIndicator.moving((screen.get_width()-30, screen.get_height()-138))
                            self.pickingBarIndicator.visible(True)
                            self.pickingbar.visible(True)

                        if player.inventory.item.reloading and player.inventory.item.reloadtime:
                            usingratio = player.inventory.item.reloaddelay / player.inventory.item.reloadtime if player.inventory.item.reloadtime else 0
                            self.usingBarIndicator.visible(False)
                            self.usingbar.visible(False)
                        else:
                            usingratio = 0
                            self.usingBarIndicator.visible(True)
                            self.usingbar.visible(True)

                        self.ammunitionvalue.visible(False)
                        self.ammunitiontypevalue.visible(False)
                        self.ammovalue.visible(False)
                        self.itemicon.visible(False)
                    
                    case 'supplies':
                        ammoratio = 0
                        maxammoratio = 0
                        ammunitionratio = player.inventory.item.amount
                        ammunitiontyperatio = player.inventory.item.itemname
                        itemiconlink = player.inventory.item.itemicon
                        self.itemIndicator.visible(False)

                        if not player.inventory.item.picked:
                            pickingratio = player.inventory.item.pickingdelay / player.inventory.item.pickingtime if player.inventory.item.pickingtime else 0
                            self.itemIndicator.moving((screen.get_width()-30, screen.get_height()-186))
                            self.pickingBarIndicator.visible(False)
                            self.pickingbar.visible(False)
                        else:
                            pickingratio = 0
                            self.itemIndicator.moving((screen.get_width()-30, screen.get_height()-138))
                            self.pickingBarIndicator.visible(True)
                            self.pickingbar.visible(True)

                        if player.inventory.item.using and player.inventory.item.usingtime:
                            usingratio = player.inventory.item.usingdelay / player.inventory.item.usingtime if player.inventory.item.usingtime else 0
                            self.usingBarIndicator.visible(False)
                            self.usingbar.visible(False)
                        else:
                            usingratio = 0
                            self.usingBarIndicator.visible(True)
                            self.usingbar.visible(True)

                        self.ammunitionvalue.visible(False)
                        self.ammunitiontypevalue.visible(False)
                        self.ammovalue.visible(False)
                        self.itemicon.visible(False)

                    case _:
                        usingratio = 0
                        ammoratio = 0
                        maxammoratio = 0
                        ammunitionratio = player.inventory.item.amount
                        ammunitiontyperatio = player.inventory.item.itemname
                        itemiconlink = player.inventory.item.itemicon
                        self.itemIndicator.visible(False)

                        if not player.inventory.item.picked:
                            pickingratio = player.inventory.item.pickingdelay / player.inventory.item.pickingtime if player.inventory.item.pickingtime else 0
                            self.itemIndicator.moving((screen.get_width()-30, screen.get_height()-186))
                            self.pickingBarIndicator.visible(False)
                            self.pickingbar.visible(False)
                        else:
                            pickingratio = 0
                            self.itemIndicator.moving((screen.get_width()-30, screen.get_height()-138))
                            self.pickingBarIndicator.visible(True)
                            self.pickingbar.visible(True)

                        self.usingBarIndicator.visible(True)
                        self.usingbar.visible(True)

                        self.ammunitionvalue.visible(False)
                        self.ammunitiontypevalue.visible(False)
                        self.ammovalue.visible(False)
                        self.itemicon.visible(False)
                      
            else:
                pickingratio = 0
                usingratio = 0
                ammoratio = 0
                maxammoratio = 0
                ammunitionratio = 0
                ammunitiontyperatio = None
                itemiconlink = "src/assets/textures/default_icon.png"
                self.itemIndicator.visible(True)
                self.pickingBarIndicator.visible(True)
                self.usingBarIndicator.visible(True)
                self.pickingbar.visible(True)
                self.usingbar.visible(True)
                self.ammunitionvalue.visible(True)
                self.ammunitiontypevalue.visible(True)
                self.ammovalue.visible(True)
                self.itemicon.visible(True)

        else:
            pickingratio = 0
            usingratio = 0
            ammoratio = 0
            maxammoratio = 0
            ammunitionratio = 0
            ammunitiontyperatio = None
            itemiconlink = "src/assets/textures/default_icon.png"
            self.itemIndicator.visible(True)
            self.pickingBarIndicator.visible(True)
            self.usingBarIndicator.visible(True)
            self.pickingbar.visible(True)
            self.usingbar.visible(True)
            self.ammunitionvalue.visible(True)
            self.ammunitiontypevalue.visible(True)
            self.ammovalue.visible(True)

        self.pickingBarIndicator.moving((self.ammovalue.headobject.rect.bottomleft[0], self.ammovalue.headobject.rect.bottomleft[1]))
        self.usingBarIndicator.moving((self.ammovalue.headobject.rect.topleft[0], self.ammovalue.headobject.rect.topleft[1]))
        self.pickingbar.moving((self.pickingbar.headobject.rect.topleft[0]+16, self.pickingbar.headobject.rect.topleft[1]+20))
        self.usingbar.moving((self.usingbar.headobject.rect.topleft[0]+16, self.usingbar.headobject.rect.topleft[1]+16))
        self.ammovalue.moving((self.ammovalue.headobject.rect.topleft[0]+364, self.ammovalue.headobject.rect.topleft[1]+52))
        self.ammunitionvalue.moving((self.ammunitionvalue.headobject.rect.topleft[0]+260, self.ammunitionvalue.headobject.rect.topleft[1]+78))
        self.ammunitiontypevalue.moving((self.ammunitiontypevalue.headobject.rect.topleft[0]+260, self.ammunitiontypevalue.headobject.rect.topleft[1]+26))
        self.itemicon.moving((self.itemicon.headobject.rect.topleft[0]+104, self.itemicon.headobject.rect.topleft[1]+52))

        self.pickingbar.sizeedit((round(384*pickingratio), 12))
        self.usingbar.sizeedit((round(384*usingratio), 12))
        self.ammunitionvalue.textedit(f'{ammunitionratio}', color=(225, 225, 255))
        self.ammunitiontypevalue.textedit(f'{ammunitiontyperatio}', color=(225, 225, 255))
        self.ammovalue.textedit(f'{ammoratio}/{maxammoratio}', color=(225, 225, 255))
        self.itemicon.imageedit(itemiconlink)