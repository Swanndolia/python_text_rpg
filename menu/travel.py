import area_list

def travel(self, player):
    print(f"Where you wanna go {player.name} ?\n Wilderness (W), Mountain (M), Desert (D), Cave (C), Town (T), Menu (0)")
    user_input = player.user_input()
    if user_input == "W":
        return area_list.wilderness.travel(self, player)
    elif user_input == "M":
        return area_list.mountain.travel(self, player)
    elif user_input == "D":
        return area_list.desert.travel(self, player)
    elif user_input == "C":
        return area_list.cave.travel(self, player)
    elif user_input == "T":
        return area_list.town.travel(self, player)
    elif user_input == "0":
        return
    else:
        return travel(self, player)
