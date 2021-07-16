import item as Item

def createItem():
    default_aquero = Item.Item()
    default_aquero.name = "Basic Bow"
    default_aquero.desc = "Default Aquero Stuff"
    default_aquero.slot = "rhand"
    default_aquero.damage = 3
    default_aquero.two_hand = True
    return default_aquero