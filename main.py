import player as Player
import enemy as Enemys
import menu
import sys

import tools as Tools

class Game():
    def __init__(self):
        self.name = "GAME"

    def main_loop(self, player):
        while True:
            self.menu_choice(player)

    def menu_choice(self, player):
        Tools.clear_console()
        Tools.printer.menu_choice(player)
        user_input = player.user_input()
        Tools.clear_console()
        if user_input == "1":
            menu.travel(self, player)
        elif user_input == "2":
            menu.inventory(self, player)
        elif user_input == "3":
            menu.spells(self, player)
        elif user_input == "4":
            menu.profile(self, player)
        else:
            self.menu_choice(player)
        return

    def restart(self):
        player = Player.Player()
        self.main_loop(player)

game = Game()

game.main_loop(Player.player)