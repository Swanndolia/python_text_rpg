import player as Player
import enemy as Enemy

from menus.menu_fight import menu_fight as menu_fight
from menus.menu_inventory import menu_inventory as menu_inventory
from menus.menu_profile import menu_profile as menu_profile
from menus.menu_skills import menu_skills as menu_skills

from tools import clear_console as Tools


class Game():
    def __init__(self):
        self.name = "GAME"

    def main_loop(self, player):
        while True:
            self.menu_choice(player)

    def menu_choice(self, player):
        Tools.clear_console()
        print("What do you want to do " + player.name +
            " ? : Fight (F), Inventory (I), Skills (S), Profile (P)")
        user_input = player.user_input()
        Tools.clear_console()
        if user_input == "F":
            menu_fight(self, player)
        elif user_input == "I":
            menu_inventory(self, player)
        elif user_input == "S":
            menu_skills(self, player)
        elif user_input == "P":
            menu_profile(self, player)
        else:
            self.menu_choice(player)
        return

game = Game()

game.main_loop(Player.player)