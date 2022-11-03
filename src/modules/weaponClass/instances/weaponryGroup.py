
from modules.weaponClass import assaultRifleWeapon, shotgunWeapon, pistolWeapon

weaponry = {

    'AK-47': assaultRifleWeapon.AssaultRifle(spreadangle=5, shotrange=600, shotspeed=600, damage=40, ammo=0, maxammo=30, ammunition=0, shooter=None, targets=None),
    'SPAS-12': shotgunWeapon.Shotgun(spreadangle=30, shotrange=400, shotspeed=240, damage=20, ammo=0, maxammo=8, ammunition=0, shooter=None, targets=None),
    'Glock-17': pistolWeapon.Pistol(spreadangle=2, shotrange=400, shotspeed=400, damage=60, ammo=0, maxammo=17, ammunition=0, shooter=None, targets=None),

}

#ТУТ ЕБАТЬ КАК НУЖНО СДЕЛАТЬ СИСТЕМУ ИНВЕНТОРЯ, ЧТОБЫ ИЮЗАТЬ ПАТРОНЫ СИММЕТРИЧНО КО ВСЕЙ ЭТОЙ ХУЙНЕ