import area_list
import tools as Tools


def travel(self, player):
    Tools.printer.ask_travel_direction(player)
    user_input = player.user_input()
    if user_input == "1":
        return area_list.wilderness.travel(self, player)
    elif user_input == "2":
        return area_list.mountain.travel(self, player)
    elif user_input == "3":
        return area_list.desert.travel(self, player)
    elif user_input == "4":
        return area_list.cave.travel(self, player)
    elif user_input == "5":
        return area_list.town.travel(self, player)
    elif user_input == "0":
        return
    else:
        return travel(self, player)
