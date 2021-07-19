import item_list
import random
import event as Event
from tools import clear_console as Tools

honey_stone = [item_list.enemy_loot.honey.createItem(), item_list.materials.stone.createItem()]

def create_event(): 
    trader = Event.Event()
    trader.name = "Trader"
    trader.desc = "I have a deal for you, lemme show you"
    trader.event_possibility = [honey_stone]
    trader.event_accepted = trade_accepted
    trader.event_declined = trade_declined
    return trader

def trade_accepted(trader, player):
    trade = random.choice(trader.event_possibility)
    print(f"Do you want to trade:\n {trade[0]} \n\nfor:\n {trade[1]}\n\nAccept (A), Deny (D)")
    user_input = player.user_input()
    Tools.clear_console()
    if(user_input == "A"):
        if(trade[0] in player.inventory):
            player.add_item_to_inventory(trade[1])
            print(f"You successfully traded: {trade[0].name} for: {trade[1].name}\n Press enter to return to menu")
            player.user_input()
        else:
            print(f"Sorry but you don't have '{trade[0].name}' in ur inventory\n Press enter to return to menu")
            player.user_input()
    elif (user_input == "D"):
        print(f"Oh okay sorry didnt't mean to bother you\n Press enter to return to menu")
        player.user_input()
    else:
        trade_accepted(player, trader)


def trade_declined(trader, player):
    Tools.clear_console()
    print(f"Oh okay sorry didnt't mean to bother you\n Press enter to return to menu")
    player.user_input()
