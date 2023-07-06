from gameCode.itemClass import suppliesClass
from gameCode.effectsClass import *

items = {

    'F. A. K.': suppliesClass.defaultSupplies.Supplies(
        itemName='F. A. K.',
        itemTextureLink=None,
        itemIconLink=None,
        secondItemType='heal',
        effectsGroup = {
            'healthInstantChangeEffect': healthInstantChangeEffect.HealthInstantChangeEffect(25),
            'healthRegenEffect': healthRegenEffect.HealthRegenEffect(5, 10)
        },
        usingTimeValue=2,
        pickingTimeValue=0.5
    ),

    'cutveins': suppliesClass.defaultSupplies.Supplies(
        itemName='cutveins',
        itemTextureLink=None,
        itemIconLink=None,
        secondItemType='damager',
        effectsGroup = {
            'healthInstantChangeEffect': healthInstantChangeEffect.HealthInstantChangeEffect(-25),
            'bleedingEffect': bleedingEffect.BleedingEffect(5, 10)
        },
        usingTimeValue=2,
        pickingTimeValue=0.5
    ),

    'Bandage': suppliesClass.defaultSupplies.Supplies(
        itemName='Bandage',
        itemTextureLink=None,
        itemIconLink=None,
        secondItemType='heal',
        effectsGroup = {
            'healthInstantChangeEffect': healthInstantChangeEffect.HealthInstantChangeEffect(10),
            'healthRegenEffect': healthRegenEffect.HealthRegenEffect(1, 10),
            'bleedingStopEffect': bleedingStopEffect.BleedingStopEffect(2, 10) #убирает по 2 секунды кровотека в течении 10 секунд
        },
        usingTimeValue=2,
        pickingTimeValue=0.5
    ),
}