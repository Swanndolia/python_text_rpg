import item_list
import random
import event as Event
import tools as Tools

honey_stone = [item_list.enemy_loot.honey.createItem(), item_list.materials.stone.createItem()]

def create_event(): 
    trader = Event.Event()
    trader.name = Tools.printer.trader_name()
    trader.desc = Tools.printer.trader_desc()
    trader.event_possibility = [honey_stone]
    trader.event_accepted = trade_accepted 
    trader.event_declined = trade_declined
    return trader

def trade_accepted(trader, player):
    trade = random.choice(trader.event_possibility)
    Tools.printer.ask_trade(trade)
    user_input = player.user_input()
    Tools.clear_console()
    if(user_input == "1"):
        if(trade[0] in player.inventory):
            player.add_item_to_inventory(trade[1])
            Tools.printer.trade_success(trade)
            player.user_input()
        else:
            Tools.printer.trade_failed(trade)
            player.user_input()
    elif (user_input == "2"):
        Tools.printer.trade_declined()
        player.user_input()
    else:
        trade_accepted(trader, player)


def trade_declined(trader, player):
    Tools.clear_console()
    Tools.printer.trade_declined()
    player.user_input()
