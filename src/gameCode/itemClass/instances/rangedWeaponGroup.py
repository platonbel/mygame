from gameCode.itemClass.weaponClass import rangedWeaponClass

items = {

    'AK-47': rangedWeaponClass.assaultRifleWeapon.AssaultRifle(
        itemName='AK-47', 
        itemTextureLink=None,
        itemIconLink="src/assets/textures/ak-47_icon.png", 
        spreadingAngleValue=5, 
        shotingRangeValue=600, 
        shotingSpeedValue=600, 
        reloadingTimeValue=3, 
        pickingTimeValue=2, 
        damageAmountValue=30, 
        bulletAmountValue=1, 
        ammoAmountValue=0, 
        maxAmmoAmountValue=30, 
        ammunitionType='7.62'
    ),
    'SPAS-12': rangedWeaponClass.pumpShotgunWeapon.PumpShotgun(
        itemName='SPAS-12',
        itemTextureLink=None,
        itemIconLink=None, 
        spreadingAngleValue=30, 
        shotingRangeValue=400, 
        shotingSpeedValue=240, 
        reloadingTimeValue=0.6, 
        pickingTimeValue=2, 
        damageAmountValue=15, 
        bulletAmountValue=8, 
        ammoAmountValue=0, 
        maxAmmoAmountValue=8, 
        ammunitionType='12/70'
    ),
    'Glock-17': rangedWeaponClass.pistolWeapon.Pistol(
        itemName='Glock-17',
        itemTextureLink=None,
        itemIconLink=None, 
        spreadingAngleValue=2, 
        shotingRangeValue=400, 
        shotingSpeedValue=400, 
        reloadingTimeValue=1, 
        pickingTimeValue=2, 
        damageAmountValue=160, 
        bulletAmountValue=1, 
        ammoAmountValue=0, 
        maxAmmoAmountValue=17, 
        ammunitionType='9x18'
    ),
    'testgun': rangedWeaponClass.assaultRifleWeapon.AssaultRifle(
        itemName='Test Gun',
        itemTextureLink=None,
        itemIconLink="src/assets/textures/testgun_icon.png", 
        spreadingAngleValue=0, 
        shotingRangeValue=600, 
        shotingSpeedValue=600, 
        reloadingTimeValue=0, 
        pickingTimeValue=0, 
        damageAmountValue=1, 
        bulletAmountValue=2, 
        ammoAmountValue=0, 
        maxAmmoAmountValue=30, 
        ammunitionType='7.62'
    ),
}