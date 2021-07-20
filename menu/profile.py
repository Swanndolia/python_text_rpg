import tools as Tools

def profile(self, player):
    Tools.printer.display_stats_profile(player)
    user_input = player.user_input()
    if(user_input == "0"):
        self.menu_choice(player)
    elif (user_input == "1"):
        player.set_stats_points()
    else:
        profile(self, player)