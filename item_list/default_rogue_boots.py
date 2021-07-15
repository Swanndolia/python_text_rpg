import item as Item

def createItem():
    default_rogue_boots = Item.Item()
    default_rogue_boots.name = "Leather Boots"
    default_rogue_boots.desc = "Default Rogue Stuff"
    default_rogue_boots.slot = "boots"
    default_rogue_boots.armor = 2
    return default_rogue_boots