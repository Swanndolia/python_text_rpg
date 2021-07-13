class Item():
    def __init__(self):
        self.name = ""
        self.desc = ""
        self.value = 0
        self.damage = 0
        self.armor = 0
        self.slot = ""
        self.two_hand = False

    def __repr__(self):
        if(self.name == ""):
            return "empty"
        else:
            return f"\nName: {self.name}\ndesc: {self.desc}\nvalue: {self.value}\ndamage: {self.damage}\narmor: {self.armor}\ntwo hands: {self.two_hand}\n"
    
default_aquero_head = Item()
default_aquero_head.name = "Leather Helmet"
default_aquero_head.desc = "Default Aquero Stuff"
default_aquero_head.slot = "head"
default_aquero_head.armor = 2
default_aquero_body = Item()
default_aquero_body.name = "Leather Armor"
default_aquero_body.desc = "Default Aquero Stuff"
default_aquero_body.slot = "body"
default_aquero_body.armor = 2
default_aquero_legs = Item()
default_aquero_legs.name = "Leather Leggings"
default_aquero_legs.desc = "Default Aquero Stuff"
default_aquero_legs.slot = "legs"
default_aquero_legs.armor = 2
default_aquero_boots = Item()
default_aquero_boots.name = "Leather Boots"
default_aquero_boots.desc = "Default Aquero Stuff"
default_aquero_boots.slot = "boots"
default_aquero_boots.armor = 2
default_aquero_weapon = Item()
default_aquero_weapon.name = "Basic Bow"
default_aquero_weapon.desc = "Default Aquero Stuff"
default_aquero_weapon.slot = "rhand"
default_aquero_weapon.damage = 3
default_aquero_weapon.two_hand = True

default_rogue_head = Item()
default_rogue_head.name = "Cloth Cap"
default_rogue_head.desc = "Default Rogue Stuff"
default_rogue_head.slot = "head"
default_rogue_head.armor = 1
default_rogue_body = Item()
default_rogue_body.name = "Leather Armor"
default_rogue_body.desc = "Default Rogue Stuff"
default_rogue_body.slot = "body"
default_rogue_body.armor = 2
default_rogue_legs = Item()
default_rogue_legs.name = "Cloth Leggings"
default_rogue_legs.desc = "Default Rogue Stuff"
default_rogue_legs.slot = "legs"
default_rogue_legs.armor = 1
default_rogue_boots = Item()
default_rogue_boots.name = "Leather Boots"
default_rogue_boots.desc = "Default Rogue Stuff"
default_aquero_boots.slot = "boots"
default_rogue_boots.armor = 2
default_rogue_weapon = Item()
default_rogue_weapon.name = "Basic Dagger"
default_rogue_weapon.desc = "Default Rogue Stuff"
default_rogue_weapon.slot = "anyhand"
default_rogue_weapon.damage = 2

default_mage_head = Item()
default_mage_head.name = "Cloth Cap"
default_mage_head.desc = "Default Mage Stuff"
default_mage_head.slot = "head"
default_mage_head.armor = 2
default_mage_body = Item()
default_mage_body.name = "Cloth Tunic"
default_mage_body.desc = "Default Mage Stuff"
default_mage_body.slot = "body"
default_mage_body.armor = 2
default_mage_legs = Item()
default_mage_legs.name = "Cloth Robe"
default_mage_legs.desc = "Default Mage Stuff"
default_mage_legs.slot = "legs"
default_mage_legs.armor = 2
default_mage_boots = Item()
default_mage_boots.name = "Leather Boots"
default_mage_boots.desc = "Default Mage Stuff"
default_mage_boots.slot = "boots"
default_mage_boots.armor = 2
default_mage_weapon = Item()
default_mage_weapon.name = "Basic Staff"
default_mage_weapon.desc = "Default Mage Stuff"
default_mage_weapon.slot = "rhand"
default_mage_weapon.damage = 5
default_mage_weapon.two_hand = True

default_warrior_head = Item()
default_warrior_head.name = "Iron Helmet"
default_warrior_head.desc = "Default Warrior Stuff"
default_warrior_head.slot = "head"
default_warrior_head.armor = 3
default_warrior_body = Item()
default_warrior_body.name = "Iron Armor"
default_warrior_body.desc = "Default Warrior Stuff"
default_warrior_body.slot = "body"
default_warrior_body.armor = 3
default_warrior_legs = Item()
default_warrior_legs.name = "Iron Leggings"
default_warrior_legs.desc = "Default Warrior Stuff"
default_warrior_legs.slot = "legs"
default_warrior_legs.armor = 3
default_warrior_boots = Item()
default_warrior_boots.name = "Iron Boots"
default_warrior_boots.desc = "Default Warrior Stuff"
default_warrior_boots.armor = 3
default_warrior_weapon = Item()
default_warrior_weapon.name = "Basic Sword"
default_warrior_weapon.desc = "Default Warrior Stuff"
default_warrior_weapon.slot = "rhand"
default_warrior_weapon.damage = 1
default_warrior_shield = Item()
default_warrior_shield.name = "Basic Shield"
default_warrior_shield.desc = "Default Warrior Stuff"
default_warrior_shield.slot = "lhand"
default_warrior_shield.armor = 3