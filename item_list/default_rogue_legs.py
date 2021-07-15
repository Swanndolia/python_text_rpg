import item as Item

def createItem():
    default_rogue_legs = Item.Item()
    default_rogue_legs.name = "Cloth Leggings"
    default_rogue_legs.desc = "Default Rogue Stuff"
    default_rogue_legs.slot = "legs"
    default_rogue_legs.armor = 1
    return default_rogue_legs