from modules.itemClass import suppliesClass

items = {

    'First Aid Kit': suppliesClass.defaultSupplies.Supplies(
        itemname='F. A. K.',
        iconimage=None,
        suppliestype='medicine',
        instanthealthheal=25,  
        healthregeneration=5, 
        healthregenerationtime=10,
        usingtime=2,
        pickingtime=0.5
    ),

    'damager': suppliesClass.defaultSupplies.Supplies(
        itemname='damager',
        iconimage=None,
        suppliestype='antiheal',
        instanthealthheal=-99,
        usingtime=2,
        pickingtime=0.5
    )
}