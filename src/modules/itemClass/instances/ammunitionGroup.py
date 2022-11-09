from modules.itemClass import ammunitionClass

items = {
    '7.62': ammunitionClass.defaultAmmunition.Ammunition(iconimage="src/assets/textures/7.62_icon.png", ammunitiontype='7.62'),
    '12/70': ammunitionClass.defaultAmmunition.Ammunition(iconimage=None, ammunitiontype='12/70'),
    '9x18': ammunitionClass.defaultAmmunition.Ammunition(iconimage=None, ammunitiontype='9x18')
}