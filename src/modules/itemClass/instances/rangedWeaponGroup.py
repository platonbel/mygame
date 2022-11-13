import pygame
from modules.itemClass.weaponClass import rangedWeaponClass

items = {

    'AK-47': rangedWeaponClass.assaultRifleWeapon.AssaultRifle(iconimage="src/assets/textures/ak-47_icon.png", spreadangle=5, shotrange=600, shotspeed=600, reloadtime=3, pickingtime=2, damage=30, bulletamount=1, ammo=0, maxammo=30),
    'SPAS-12': rangedWeaponClass.pumpShotgunWeapon.PumpShotgun(iconimage=None, spreadangle=30, shotrange=400, shotspeed=240, reloadtime=0.6, pickingtime=2, damage=20, bulletamount=8, ammo=0, maxammo=8),
    'Glock-17': rangedWeaponClass.pistolWeapon.Pistol(iconimage=None, spreadangle=2, shotrange=400, shotspeed=400, reloadtime=1, damage=60, pickingtime=1, ammo=0, bulletamount=1, maxammo=17),
    'testgun': rangedWeaponClass.assaultRifleWeapon.AssaultRifle(iconimage="src/assets/textures/testgun_icon.png", spreadangle=5, shotrange=600, shotspeed=600, reloadtime=0, pickingtime=0, damage=1, bulletamount=1, ammo=0, maxammo=30),
}