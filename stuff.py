import item as Item
from item_list import *

class Stuff():
    def __init__(self):
        self.head = head
        self.body = body
        self.legs = legs
        self.boots = boots
        self.rhand = rhand
        self.lhand = lhand

    def __repr__(self):
        return f"\nHead: {self.head}\nBody: {self.body}\nLlegs: {self.legs}\nBoots: {self.boots}\nLeft Hand: {self.lhand}\nRight Hand: {self.rhand}\n"
    
    def set_warrior_stuff(self):
        self.head = default_warrior_head.default_warrior_head
        self.body = default_warrior_body.default_warrior_body
        self.legs = default_warrior_legs.default_warrior_legs
        self.boots = default_warrior_boots.default_warrior_boots
        self.rhand = default_warrior_weapon.default_warrior_weapon
        self.lhand = default_warrior_shield.default_warrior_shield


    def set_aquero_stuff(self):
        self.head = default_aquero_head.default_aquero_head
        self.body = default_aquero_body.default_aquero_body
        self.legs = default_aquero_legs.default_aquero_legs
        self.boots = default_aquero_boots.default_aquero_boots
        self.rhand = default_aquero_weapon.default_aquero_weapon
        if(self.rhand.two_hand):
            self.lhand = self.rhand
    
    def set_rogue_stuff(self):
        self.head = default_rogue_head.default_rogue_head
        self.body = default_rogue_body.default_rogue_body
        self.legs = default_rogue_legs.default_rogue_legs
        self.boots = default_rogue_boots.default_rogue_boots
        self.rhand = default_rogue_weapon.default_rogue_weapon
        self.lhand = default_rogue_weapon.default_rogue_weapon
        if(self.rhand.two_hand):
            self.lhand = self.rhand

    def set_mage_stuff(self):
        self.head = default_mage_head.default_mage_head
        self.body = default_mage_body.default_mage_body
        self.legs = default_mage_legs.default_mage_legs
        self.boots = default_mage_boots.default_mage_boots
        self.rhand = default_mage_weapon.default_mage_weapon
        if(self.rhand.two_hand):
            self.lhand = self.rhand


head = Item.Item()
body = Item.Item()
legs = Item.Item()
boots = Item.Item()
lhand = Item.Item()
rhand = Item.Item()
