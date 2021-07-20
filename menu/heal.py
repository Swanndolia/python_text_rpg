import tools as Tools

def heal(self, player):
    cost = round(1+ (player.health[1] - player.health[0]) / 10)
    Tools.printer.ask_heal(player, cost)
    user_input = player.user_input()
    if(user_input == "0"):
        self.menu_choice(player)
    elif (user_input == "1"):
        if(player.gold >= cost):
            player.health[0] = player.health[1]
            player.gold -= cost
            Tools.printer.success_heal()
        else:
            Tools.printer.not_enough_gold(player, cost)
        player.user_input()
    else:
        heal(self, player)
