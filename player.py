import stuff as Stuff
from tools import clear_console as Tools

class Player():
    def __init__(self):
        self.name = input("> What's ur name ? ")
        self.build = ""
        self.lvl = 1
        self.exp = 0
        self.next_lvl_exp = 100
        self.health = 100
        self.mana = 100
        self.agility = 0
        self.strength = 0
        self.dexterity = 0
        self.speed = 0
        self.luck = 0
        self.skills = []
        self.stuff = Stuff.stuff
        self.inventory = []

    def __repr__(self):
        return f"\nname: {self.name}\nclass: {self.build}\nnext level: {self.next_lvl_exp - self.exp} xp\nhealth: {self.health}\nmana: {self.mana}\nagility: {self.agility}\nstrength: {self.strength}\ndexterity: {self.dexterity}\nspeed: {self.speed}\nluck: {self.luck}\n"

    def user_input(self):
        user_input = input("> ").upper()
        return user_input

    def build_choice(self, player):
        Tools.clear_console()
        print("Which class you prefer " + player.name +
              " ? : Mage (M), Warrior (W), rogue (R), Aquero (A) \nCare you can't change this later !")
        user_input = player.user_input()
        if user_input == "M":
            Stuff.stuff.set_mage_stuff()
            return "Mage"
        elif user_input == "W":
            Stuff.stuff.set_warrior_stuff()
            return "Warrior"
        elif user_input == "R":
            Stuff.stuff.set_rogue_stuff()
            return "Rogue"
        elif user_input == "A":
            Stuff.stuff.set_aquero_stuff()
            return "Aquero"
        else:
            print("error, please use one of the following key : M, W, R, A")
            self.build_choice(player)

player = Player()

if(player.build == ""):
    player.build = player.build_choice(player)