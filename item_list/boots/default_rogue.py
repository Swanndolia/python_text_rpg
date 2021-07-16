import item as Item

def createItem():
    default_rogue = Item.Item()
    default_rogue.name = "Leather Boots"
    default_rogue.desc = "Default Rogue Stuff"
    default_rogue.slot = "boots"
    default_rogue.armor = 2
    return default_rogue