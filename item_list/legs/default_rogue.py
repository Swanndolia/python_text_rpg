import item as Item

def createItem():
    default_rogue = Item.Item()
    default_rogue.name = "Cloth Leggings"
    default_rogue.desc = "Default Rogue Stuff"
    default_rogue.slot = "legs"
    default_rogue.armor = 1
    return default_rogue