import item as Item

def createItem():
    default_mage_head = Item.Item()
    default_mage_head.name = "Cloth Cap"
    default_mage_head.desc = "Default Mage Stuff"
    default_mage_head.slot = "head"
    default_mage_head.armor = 2
    return default_mage_head