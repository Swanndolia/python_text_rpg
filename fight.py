import tools as Tools
import random

def fight(self, player, enemy):
    if(enemy.health > 0 and player.health[0] > 0):
        Tools.printer.fighting_turn(player, enemy)
        user_input = player.user_input()
        Tools.clear_console()
        if (user_input == "1"):
            if(player.rapidity > enemy.rapidity):
                player_attack(self, player, enemy)
                enemy_attack(self, player, enemy)
                fight(self, player, enemy)
            else:
                enemy_attack(self, player, enemy)
                player_attack(self, player, enemy)
                fight(self, player, enemy)
        elif (user_input == "2"):
            fight(self, player, enemy)
        elif (user_input == "3"):
            fight(self, player, enemy)
        elif (user_input == "4"):
            if(player_try_flee(self, player, enemy)):
                return self.menu_choice(player)
            fight(self, player, enemy)
        else:
            fight(self, player, enemy)
    else:
        return self.menu_choice(player)


def enemy_attack(self, player, enemy):
    damage = enemy.strength - round(player.armor / 8)
    if(enemy.strength > round(player.armor / 8)):
        player.health[0] -= damage
        print(f"{enemy.name} inflicted you {damage} damage")
    else:
        print(f"Your armor absorbed all the damage from the {enemy.name}")
    if(player.health[0] <= 0):
        player_is_dead(self, player, enemy)


def player_attack(self, player, enemy):
    if(player.stuff.rhand.two_hand):
        damage = player.stuff.rhand.damage
    else:
        damage = player.stuff.rhand.damage * 2 + round(player.strength / 3)
    if(damage > round(enemy.armor / 8)):
        enemy.health -= damage
        print(f"You inflicted you {damage} damage to {enemy.name}")
    else:
        print(
            f"You didn't scratched the {enemy.name}, it's armor is too strong !")
    if(enemy.health <= 0):
        enemy_is_dead(self, player, enemy)


def player_try_flee(self, player, enemy):
    if(enemy.rapidity / (player.rapidity + 1) > 0.5):
        enemy_attack(self, player, enemy)
        print("The enemy is too fast, you can't flee")
        return False
    elif (player.rapidity / (enemy.rapidity + 1) > 0.5):
        print(f"You're so fast ! The {enemy.name} will never catch you back")
        return True
    else:
        if(enemy.rapidity >= player.rapidity):
            enemy_attack(self, player, enemy)
        if(random.randint(0, 100) > 50):
            print("You got lucky and achieved to escape\nPress enter to return to menu")
            player.user_input()
            return True
        else:
            print("Unlucky ! The enemy predicted your move and didn't let you escape")
            return False


def enemy_is_dead(self, player, enemy):
    print(f"{player.name} has killed {enemy.name}, you've won: {enemy.reward_gold} gold and {enemy.reward_exp} xp")
    player.gold += enemy.reward_gold
    player.exp += enemy.reward_exp
    if(player.exp >= player.next_lvl_exp):
        player.next_lvl_exp += round(player.next_lvl_exp * 1.1)
        player.unasigned_stats += 1
        player.lvl += 1
        print(f"Amazing ! you're now lvl {player.lvl}")
    player.mana[0] = player.mana[1]
    for x in enemy.loot:
        if(random.randint(1, 1000) <= x[0]):
            player.add_item_to_inventory(x[1])
            print(f"You've found {x[1].name} on the {enemy.name}")
    print("Press enter to return to menu")
    player.user_input()

def player_is_dead(self, player, enemy):
    print(f"{enemy.name} has killed {player.name}")
    print("Press enter to start a new game")
    player.user_input()
    Tools.clear_console()
    return self.restart()
