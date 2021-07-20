from fight import fight

import tools as Tools

import random
import enemy_list
import event_list


def travel(self, player):
    Tools.clear_console()
    if (random.randint(1, 100) <= 10):
        select_event(self, player)
    else:
        select_enemy(self, player)


def select_event(self, player):
    selected_event = random.choice(
        [x for x in dir(event_list.wilderness) if not x.startswith('__')])
    event = getattr(event_list.wilderness, selected_event).create_event()
    Tools.printer.event_happen(event, player)
    user_input = player.user_input()
    Tools.clear_console()
    if (user_input == "1"):
        event.event_accepted(event, player)
    elif (user_input == "2"):
        event.event_declined(event, player)
    else:
        travel(self, player)


def select_enemy(self, player):
    selected_enemy = random.choice(
        [x for x in dir(enemy_list.wilderness) if not x.startswith('__')])
    enemy = getattr(enemy_list.wilderness, selected_enemy).create_enemy(
        random.randint(1, 9))
    Tools.printer.enemy_found(player, enemy)
    user_input = player.user_input()
    Tools.clear_console()
    if (user_input == "1"):
        return fight(self, player, enemy)
    elif (user_input == "2"):
        return travel(self, player)
    elif (user_input == "0"):
        return
    else:
        return travel(self, player)
