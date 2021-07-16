import item as Item

def createItem():
    default_mage = Item.Item()
    default_mage.name = "Cloth Tunic"
    default_mage.desc = "Default Mage Stuff"
    default_mage.slot = "body"
    default_mage.armor = 2
    return default_mage