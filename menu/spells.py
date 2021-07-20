import tools as Tools

def spells(self, player):
    Tools.printer.show_player_spells(player)
    if(player.user_input() == "0"):
        self.menu_choice(player)