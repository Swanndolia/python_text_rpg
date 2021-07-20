import tools as Tools
import menu

def travel(self, player):
    Tools.clear_console()
    Tools.printer.arrive_town(player)
    user_input = player.user_input()
    if (user_input == "1"):
        Tools.clear_console()
        menu.shop(self, player)
    elif (user_input == "2"):
        Tools.clear_console()
        menu.heal(self, player)
    elif (user_input == "0"):
        return
    else:
        travel(self, player)