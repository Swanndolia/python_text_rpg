import item as Item

def createItem():
    default_rogue_weapon = Item.Item()
    default_rogue_weapon.name = "Basic Dagger"
    default_rogue_weapon.desc = "Default Rogue Stuff"
    default_rogue_weapon.slot = "anyhand"
    default_rogue_weapon.damage = 2
    return default_rogue_weapon