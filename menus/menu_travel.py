import areas

def menu_travel(self, player):
    print("Where you wanna go " + player.name +
            " ? : Wilderness (W), Mountain (M), Desert (D), Cave (C)")
    print("Press 0 to return to menu")
    user_input = player.user_input()
    if user_input == "W":
        areas.wilderness.travel(self, player)
    elif user_input == "M":
        areas.mountain.travel(self, player)
    elif user_input == "D":
        areas.desert.travel(self, player)
    elif user_input == "C":
        areas.cave.travel(self, player)
    else:
        menu_travel(self, player)
