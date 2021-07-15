import item as Item

def createItem():
    default_mage_boots = Item.Item()
    default_mage_boots.name = "Leather Boots"
    default_mage_boots.desc = "Default Mage Stuff"
    default_mage_boots.slot = "boots"
    default_mage_boots.armor = 2
    return default_mage_boots