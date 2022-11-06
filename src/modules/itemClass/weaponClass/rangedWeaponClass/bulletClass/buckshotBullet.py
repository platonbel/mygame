from . import defaultBullet

def Buckshot(owner, targets, mouse, spreadangle, shotrange, damage, amount=8):
    for i in range(amount):
        defaultBullet.Bullet(owner=owner, targets=targets, mouse=mouse, spreadangle=spreadangle, shotrange=shotrange, damage=damage)
