import item as Item

def createItem():
    default_rogue_head = Item.Item()
    default_rogue_head.name = "Cloth Cap"
    default_rogue_head.desc = "Default Rogue Stuff"
    default_rogue_head.slot = "head"
    default_rogue_head.armor = 1
    return default_rogue_head