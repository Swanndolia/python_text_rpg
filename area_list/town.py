from tools import clear_console as Tools
import menu

def travel(self, player):
    Tools.clear_console()
    print("What you wanna do " + player.name +
          " ? : Shop (S), Heal (H)")
    print("Press 0 to return to menu")
    user_input = player.user_input()
    if (user_input == "S"):
        Tools.clear_console()
        menu.shop(self, player)
    elif (user_input == "H"):
        Tools.clear_console()
        menu.heal(self, player)
    elif (user_input == "0"):
        return
    else:
        travel(self, player)