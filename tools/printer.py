import gettext
_ = gettext.gettext


def your_inventory():
    print(_("This is your inventory:"))

def your_equiped_stuff(player):
    print(_(f"This is your equiped stuff:\n{player.stuff}"))

def fighting_turn(player, enemy):
    print(_(
        f"{player.name}: {player.health[0]} HP / {enemy.name}: {enemy.health} HP\nWhat you want to do {player.name} ? Attack(1), Spell(2), Item(3), Flee(4)"))


def display_stats_profile(player):
    print(
        _(f"This is you:\n{player}\nPress 1 to set unnasigned stats points ({player.unasigned_stats})"))


def ask_travel_direction(player):
    print(
        _(f"Where you wanna go {player.name} ?\n Wilderness (1), Mountain (2), Desert (3), Cave (4), Town (5), Menu (0)"))


def trader_name():
    return _("Trader")


def trader_desc():
    return _("I have a deal for you, lemme show you")


def ask_trade(trade):
    print(_(
        f"Do you want to trade:\n {trade[0]} \n\nfor:\n {trade[1]}\n\nAccept (1), Deny (2)"))


def trade_success(trade):
    print(
        _(f"You successfully traded: {trade[0].name} for: {trade[1].name}"))


def trade_failed(trade):
    print(
        _(f"Sorry but you don't have '{trade[0].name}' in ur inventory"))


def trade_declined():
    print(_(f"Oh okay sorry didnt't mean to bother you"))


def not_enough_gold(player, cost):
    print(
        _(f"You dont have enough gold ({player.gold} / {cost}) !"))


def success_heal():
    print(_("You've been successfully healed !"))


def ask_heal(player, cost):
    print(
        _(f"Hello {player.name}, you currently have {player.health[0]} HP\nPress 1 to heal all your hp ({player.health[0]} / {player.health[1]}) it will cost you {cost} gold."))


def arrive_town(player):
    print(
        _(f"What you wanna do {player.name} ? Shop (1), Heal (2), Menu (0)"))


def enemy_found(player, enemy):
    print(
        _(f"You encountered a {enemy.name} lvl {enemy.lvl} {enemy.desc}\n What you wanna do {player.name} ? Fight (1), Explore More (2)"))


def event_happen(event, player):
    print(_(f"A {event.name} stop you, {event.desc}\n What you wanna do {player.name} ? Accept (1), Deny (2)"))

def show_player_spells(player):
    print(_(f"This is the list of your spells: {player.spells}"))


def menu_choice(player):
    print(
        _(f"What do you want to do {player.name} ?\n Travel (1), Inventory (2), Spells (3), Profile (4)"))


def assign_stats(self):
    print(_(
        f"Remaining stats points: ({self.unasigned_stats})\n(1) Health: {self.health[0]} / {self.health[1]}\n(2) Mana: {self.mana[0]} / {self.mana[1]}\n(3) Agility: {self.agility}\n(4) Strength: {self.strength}\n(5) Dexterity: {self.dexterity}\n(6) Rapidity: {self.rapidity}\n(7) Luck: {self.luck}\n"))


def build_choice(self):
    print(
        _(f"Which class you prefer {self.name} ?\n Mage (1), Warrior (2), rogue (3), Aquero (4) \n  Care you can't change this later !"))


def whats_your_name():
    return input(_("> What's ur name ? "))


def save_found():
    print(_("We found a save load it (1) ? or no (2) ?\n Selecting '2' and keep playing will erase it"))


def repr_stuff(self):
    return _(f"\nHead: {self.head}\nBody: {self.body}\nLlegs: {self.legs}\nBoots: {self.boots}\nLeft Hand: {self.lhand}\nRight Hand: {self.rhand}\n")


def repr_spells(self):
    return _(f"\nid: {self.id}\nname: {self.name}\ndesc: {self.desc}\ndamage: {self.damage}\nmp cost: {self.mp_cost}\n")


def repr_player(self):
    return _(f"\nName: {self.name}\nClass: {self.build}\nLevel: {self.lvl}\nGold: {self.gold}\nNext Level: {self.next_lvl_exp - self.exp} XP\nHealth: {self.health[0]} / {self.health[1]} \nMana: {self.mana[0]} / {self.mana[1]}\nAgility: {self.agility}\nStrength: {self.strength}\nDexterity: {self.dexterity}\nSpeed: {self.rapidity}\nLuck: {self.luck}\n")


def repr_item(self):
    if(self.two_hand):
        if_two_hands = _(f"Two Handed\n")
    else:
        if_two_hands = ""
    if(self.damage):
        if_damage = _(f"\nDamage: {self.damage}\n")
    else:
        if_damage = ""
    if(self.armor):
        if_armor = _(f"\nArmor: {self.armor}\n")
    else:
        if_armor = ""
    return _(f"\nName: {self.name}\nDesc: {self.desc}\nValue: {self.value}{if_damage}{if_armor}{if_two_hands}")