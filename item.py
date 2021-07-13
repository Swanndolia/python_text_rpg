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
            if_two_hands = "Two Handed\n"
        else:
            if_two_hands = ""
        if(self.name == ""):
            return "Empty"
        else:
            return f"\nName: {self.name}\ndesc: {self.desc}\nvalue: {self.value}\ndamage: {self.damage}\narmor: {self.armor}\n" + if_two_hands
