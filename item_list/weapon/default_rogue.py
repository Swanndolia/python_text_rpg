import item as Item

def createItem():
    default_rogue = Item.Item()
    default_rogue.name = "Basic Dagger"
    default_rogue.desc = "Default Rogue Stuff"
    default_rogue.slot = "anyhand"
    default_rogue.damage = 2
    return default_rogue