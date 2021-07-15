import area_list

def travel(self, player):
    print("Where you wanna go " + player.name +
            " ? : Wilderness (W), Mountain (M), Desert (D), Cave (C), Town (T)")
    print("Press 0 to return to menu")
    user_input = player.user_input()
    if user_input == "W":
        area_list.wilderness.travel(self, player)
    elif user_input == "M":
        area_list.mountain.travel(self, player)
    elif user_input == "D":
        area_list.desert.travel(self, player)
    elif user_input == "C":
        area_list.cave.travel(self, player)
    elif user_input == "T":
        area_list.town.travel(self, player)
    else:
        travel(self, player)
