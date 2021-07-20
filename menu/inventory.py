import tools as Tools

def inventory(self, player):
    Tools.printer.your_inventory()
    for (i, item) in enumerate(player.inventory, start=1):
        print(f"ID: {i} {item}")
    Tools.printer.your_equiped_stuff(player)
    user_input = player.user_input()
    if(user_input == "0"):
        self.menu_choice(player)