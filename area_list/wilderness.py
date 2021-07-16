from fight import fight

from tools import clear_console as Tools

import random
import enemy_list

def travel(self, player):
    Tools.clear_console()
    selected_enemy = random.choice(
        [x for x in dir(enemy_list.wilderness) if not x.startswith('__')])
    enemy = getattr(enemy_list.wilderness, selected_enemy).create_enemy(
        random.randint(1, 9))
    print(f"You encountered a {enemy.name} lvl {enemy.lvl} {enemy.desc}\nWhat you wanna do {player.name} ? Fight (F), Explore More (E)\nElse, press 0 to return to menu")
    user_input = player.user_input()
    if (user_input == "F"):
        Tools.clear_console()
        return fight(self, player, enemy)
    elif (user_input == "E"):
        return travel(self, player)
    elif (user_input == "0"):
        return
    else:
        return travel(self, player)
