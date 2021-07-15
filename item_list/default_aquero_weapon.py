import item as Item

def createItem():
    default_aquero_weapon = Item.Item()
    default_aquero_weapon.name = "Basic Bow"
    default_aquero_weapon.desc = "Default Aquero Stuff"
    default_aquero_weapon.slot = "rhand"
    default_aquero_weapon.damage = 3
    default_aquero_weapon.two_hand = True
    return default_aquero_weapon