import stuff as Stuff
from tools import clear_console as Tools

class Player():
    def __init__(self):
        self.name = input("> What's ur name ? ")
        self.build = self.build_choice()
        self.lvl = 1
        self.exp = 0
        self.gold = 0
        self.unasigned_stats = 12
        self.next_lvl_exp = 100
        self.health = [100, 100]
        self.mana = [100, 100]
        self.agility = 0
        self.strength = 0
        self.dexterity = 0
        self.rapidity = 0
        self.luck = 0
        self.skills = []
        self.stuff = stuff
        self.inventory = []
        self.armor = self.calc_player_armor()

    def __repr__(self):
        return f"\n\nName: {self.name}\n\nClass: {self.build}\n\nGold: {self.gold}\n\nNext Level: {self.next_lvl_exp - self.exp} XP\n\nHealth: {self.health[0]} / {self.health[1]} \n\nMana: {self.mana[0]} / {self.mana[1]}\n\nAgility: {self.agility}\n\nStrength: {self.strength}\n\nDexterity: {self.dexterity}\n\nSpeed: {self.rapidity}\n\nLuck: {self.luck}\n\n"

    def user_input(self):
        user_input = input("> ").upper()
        return user_input

    def build_choice(self):
        Tools.clear_console()
        print("Which class you prefer " + self.name +
              " ? : Mage (M), Warrior (W), rogue (R), Aquero (A) \n\nCare you can't change this later !")
        user_input = self.user_input()
        if user_input == "M":
            stuff.set_mage_stuff()
            return "Mage"
        elif user_input == "W":
            stuff.set_warrior_stuff()
            return "Warrior"
        elif user_input == "R":
            stuff.set_rogue_stuff()
            return "Rogue"
        elif user_input == "A":
            stuff.set_aquero_stuff()
            return "Aquero"
        else:
            print("error, please use one of the following key : M, W, R, A")
            self.build_choice()

    def add_item_to_inventory(self, item):
        player.inventory.append(item)

    def calc_player_armor(self):
        return self.stuff.body.armor + self.stuff.boots.armor + self.stuff.head.armor + self.stuff.legs.armor + self.stuff.lhand.armor

    def equip_item(self, item):
        if(item.slot == "head"):
            if(stuff.head.name != ""):
                self.inventory.append(stuff.head)
            stuff.head = item

        elif(item.slot == "body"):
            if(stuff.body.name != ""):
                self.inventory.append(stuff.body)
            stuff.body = item

        elif(item.slot == "legs"):
            if(stuff.legs.name != ""):
                self.inventory.append(stuff.legs)
            stuff.legs = item

        elif(item.slot == "boots"):
            if(stuff.boots.name != ""):
                self.inventory.append(stuff.boots)
            stuff.boots = item

        elif(item.slot == "rhand"):
            if(stuff.rhand.name != ""):
                self.inventory.append(stuff.rhand)
            stuff.rhand = item

        elif(item.slot == "lhand"):
            if(stuff.lhand.name != ""):
                self.inventory.append(stuff.lhand)
            stuff.lhand = item

        elif(item.slot == "anyhand"):
            # TODO
            return

    def set_stats_points(self):

        if(self.unasigned_stats != 0):
            Tools.clear_console()
            print("Remaining stats points: " + str(self.unasigned_stats) +
                  f"\n\n(H) Health: {self.health}\n\n(M) Mana: {self.mana[0]} / {self.mana[1]}\n\n(A) Agility: {self.agility}\n\n(S) Strength: {self.strength}\n\n(D) Dexterity: {self.dexterity}\n\n(R) Rapidity: {self.rapidity}\n\n(L) Luck: {self.luck}")
            print("Press 0 to return to menu")
            user_input = self.user_input()
            if(user_input == "H"):
                self.health[1] += 10
                self.unasigned_stats -= 1
            elif(user_input == "M"):
                self.mana[1] += 10
                self.unasigned_stats -= 1
            elif(user_input == "A"):
                self.agility += 1
                self.unasigned_stats -= 1
            elif(user_input == "S"):
                self.strength += 1
                self.unasigned_stats -= 1
            elif(user_input == "R"):
                self.rapidity += 1
                self.unasigned_stats -= 1
            elif(user_input == "D"):
                self.dexterity += 1
                self.unasigned_stats -= 1
            elif(user_input == "L"):
                self.luck += 1
                self.unasigned_stats -= 1
            elif(user_input == "0"):
                return
            self.set_stats_points()
        else:
            Tools.clear_console()
            print("You don't have unasigned stats points, press enter to return to menu")
            input()
            return


Tools.clear_console()

stuff = Stuff.Stuff()

player = Player()
