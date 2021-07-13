import player as Player
import item as Item

class Stuff():
    def __init__(self):
        self.head = head
        self.body = body
        self.legs = legs
        self.boots = boots
        self.rhand = rhand
        self.lhand = lhand

    def __repr__(self):
        return f"\nHead: {self.head}\nbody: {self.body}\nlegs: {self.legs}\nboots: {self.boots}\nlhand: {self.lhand}\nrhand: {self.rhand}\n"
    
    def set_warrior_stuff(self):
        self.head = Item.default_warrior_head
        self.body = Item.default_warrior_body
        self.legs = Item.default_warrior_legs
        self.boots = Item.default_warrior_boots
        self.rhand = Item.default_warrior_weapon
        self.lhand = Item.default_warrior_shield


    def set_aquero_stuff(self):
        self.head = Item.default_aquero_head
        self.body = Item.default_aquero_body
        self.legs = Item.default_aquero_legs
        self.boots = Item.default_aquero_boots
        self.rhand = Item.default_aquero_weapon
        if(self.rhand.two_hand):
            self.lhand = self.rhand
    
    def set_rogue_stuff(self):
        self.head = Item.default_rogue_head
        self.body = Item.default_rogue_body
        self.legs = Item.default_rogue_legs
        self.boots = Item.default_rogue_boots
        self.rhand = Item.default_rogue_weapon
        self.lhand = Item.default_rogue_weapon
        if(self.rhand.two_hand):
            self.lhand = self.rhand

    def set_mage_stuff(self):
        self.head = Item.default_mage_head
        self.body = Item.default_mage_body
        self.legs = Item.default_mage_legs
        self.boots = Item.default_mage_boots
        self.rhand = Item.default_mage_weapon
        if(self.rhand.two_hand):
            self.lhand = self.rhand

    def equip_item(self, item, player):
        if(item.slot == "head"):
            if(self.head.name != ""):
                Player.player.inventory.append(self.head)
            self.head = item

        elif(item.slot == "body"):
            if(self.body.name != ""):
                Player.player.inventory.append(self.body)
            self.body = item

        elif(item.slot == "legs"):
            if(self.legs.name != ""):
                Player.player.inventory.append(self.legs)
            self.legs = item

        elif(item.slot == "boots"):
            if(self.boots.name != ""):
                Player.player.inventory.append(self.boots)
            self.boots = item

        elif(item.slot == "rhand"):
            if(self.rhand.name != ""):
                Player.player.inventory.append(self.rhand)
            self.rhand = item

        elif(item.slot == "lhand"):
            if(self.lhand.name != ""):
                Player.player.inventory.append(self.lhand)
            self.lhand = item

        elif(item.slot == "anyhand"):
            #TODO
            return


head = Item.Item()
body = Item.Item()
legs = Item.Item()
boots = Item.Item()
lhand = Item.Item()
rhand = Item.Item()

stuff = Stuff()
