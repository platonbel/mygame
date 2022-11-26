from modules.itemClass import ammunitionClass

items = {
    '7.62': ammunitionClass.defaultAmmunition.Ammunition(
        itemname='7.62',
        iconimage="src/assets/textures/7.62_icon.png", 
        ammunitiontype='7.62',
        pickingtime=0
    ),
    '12/70': ammunitionClass.defaultAmmunition.Ammunition(
        itemname='12/70',
        iconimage=None, 
        ammunitiontype='12/70',
        pickingtime=0
    ),
    '9x18': ammunitionClass.defaultAmmunition.Ammunition(
        itemname='9x18',
        iconimage=None, 
        ammunitiontype='9x18',
        pickingtime=0
    ),
    'default': ammunitionClass.defaultAmmunition.Ammunition(
        itemname='default',
        iconimage=None, 
        ammunitiontype='default',
        pickingtime=0
    )
}