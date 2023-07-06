from gameCode.itemClass import ammunitionClass

items = {
    '7.62': ammunitionClass.defaultAmmunition.Ammunition(
        itemName='7.62 к.',
        itemTextureLink=None,
        itemIconLink="src/assets/textures/7.62_icon.png", 
        secondItemType='7.62',
        pickingTimeValue=0
    ),
    '12/70': ammunitionClass.defaultAmmunition.Ammunition(
        itemName='12/70 к.',
        itemTextureLink=None,
        itemIconLink=None, 
        secondItemType='12/70',
        pickingTimeValue=0
    ),
    '9x18': ammunitionClass.defaultAmmunition.Ammunition(
        itemName='9x18 к.',
        itemTextureLink=None,
        itemIconLink=None, 
        secondItemType='9x18',
        pickingTimeValue=0
    ),
    'default': ammunitionClass.defaultAmmunition.Ammunition(
        itemName='default к.',
        itemTextureLink=None,
        itemIconLink=None, 
        secondItemType='default',
        pickingTimeValue=0
    )
}