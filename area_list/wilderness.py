from fight import fight

from tools import clear_console as Tools

import random
import enemy_list
import event_list

def travel(self, player):
    Tools.clear_console()
    if (random.randint(1, 100) <= 10):
        selected_event = random.choice(
            [x for x in dir(event_list.wilderness) if not x.startswith('__')])
        event = getattr(event_list.wilderness, selected_event).create_event()
        print(f"A {event.name} stop you, {event.desc}\n What you wanna do {player.name} ? Accept (A), Deny (D)")
        user_input = player.user_input()
        Tools.clear_console()
        if (user_input == "A"):
            return event.event_accepted(event, player)
        elif (user_input == "D"):
            return event.event_declined(event, player)
        else:
            return travel(self, player)
    else:
        selected_enemy = random.choice(
            [x for x in dir(enemy_list.wilderness) if not x.startswith('__')])
        enemy = getattr(enemy_list.wilderness, selected_enemy).create_enemy(
            random.randint(1, 9))
        print(
            f"You encountered a {enemy.name} lvl {enemy.lvl} {enemy.desc}\n What you wanna do {player.name} ? Fight (F), Explore More (E)\n  Else, press 0 to return to menu")
        user_input = player.user_input()
        Tools.clear_console()
        if (user_input == "F"):
            return fight(self, player, enemy)
        elif (user_input == "E"):
            return travel(self, player)
        elif (user_input == "0"):
            return
        else:
            return travel(self, player)
