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
        if(self.two_hand):
            if_two_hands = "\nTwo Handed"
        else:
            if_two_hands = ""
        if(self.damage):
            if_damage = "\ndamage: {self.damage}"
        else:
            if_damage = ""
        if(self.armor):
            if_armor = "\ndamage: {self.armor}"
        else:
            if_armor = ""
        if(self.name == ""):
            return "Empty"
        else:
            return f"\nName: {self.name}\ndesc: {self.desc}\nvalue: {self.value} {if_damage} {if_armor} {if_two_hands}"
