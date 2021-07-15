from fight import fight

from tools import clear_console as Tools

import random
import enemy_list

def travel(self, player):
    Tools.clear_console()
    selected_enemy = random.choice([x for x in dir(enemy_list) if not x.startswith('__')])
    enemy = getattr(enemy_list, selected_enemy).create_enemy(random.randint(1, 9))
    print("You encountered a lvl " + str(enemy.lvl) +
          " " + enemy.name + " " + enemy.desc)
    print("What you wanna do " + player.name +
          " ? : Fight (F), Explore More (E)")
    user_input = player.user_input()
    if (user_input == "F"):
        fight(player, enemy)
    elif (user_input == "E"):
        travel(self, player)
    elif (user_input == "0"):
        return
