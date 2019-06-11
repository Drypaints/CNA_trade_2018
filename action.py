#! /usr/bin/env python3

## red == close < open

def get_avg(data):
    res = float(0)
    if (len(data) > 7):
        for i in range(-7, 0):
            res += data[i]
        res /= 7
    else:
        for elt in data:
            res += elt
        res /= len(data)
    return res

def get_avg_50(data):
    res = float(0)
    if (len(data) > 50):
        for i in range(-50, 0):
            res += data[i]
        res /= 50
    else:
        for elt in data:
            res += elt
        res /= len(data)
    return res

def start_action(game_obj):
    game_obj.s_transaction_fee_percent = 1 - float(game_obj.s_transaction_fee_percent)
    BTC = game_obj.game_candles_usdt_btc
    BTC_avg = get_avg(BTC)
    BTC_avg_50 = get_avg_50(BTC)
    ETH = game_obj.game_candles_usdt_eth
    ETH_avg = get_avg(ETH)
    ETH_avg_50 = get_avg_50(ETH)
    USD = game_obj.game_candles_btc_eth
    USD_avg = get_avg(USD)
    USD_avg_50 = get_avg_50(USD)
    if (BTC_avg < float(BTC[-1]) and BTC_avg_50 < float(BTC[-1]) and game_obj.stock_btc != 0):
        print("sell USDT_BTC {}".format(game_obj.stock_btc))
        game_obj.s_initial_stack += game_obj.stock_btc * float(BTC[-1])
        game_obj.stock_btc = 0
    elif (BTC_avg > float(BTC[-1]) and BTC_avg_50 > float(BTC[-1]) and game_obj.s_initial_stack > 0):
        print("buy USDT_BTC 0.0001")
        game_obj.stock_btc += 0.0001 * float(game_obj.s_transaction_fee_percent)
        game_obj.s_initial_stack -= 0.0001 * float(BTC[-1])
    elif (ETH_avg < float(ETH[-1]) and ETH_avg_50 < float(ETH[-1]) and game_obj.stock_eth != 0):
        print("sell USDT_ETH {}".format(game_obj.stock_eth))
        game_obj.s_initial_stack += game_obj.stock_eth * float(ETH[-1])
        game_obj.stock_eth = 0
    elif (ETH_avg > float(ETH[-1]) and ETH_avg_50 > float(ETH[-1]) and game_obj.s_initial_stack > 0):
        print("buy USDT_ETH 0.0001")
        game_obj.stock_eth += 0.0001 * float(game_obj.s_transaction_fee_percent)
        game_obj.s_initial_stack -= 0.0001 * float(ETH[-1])
    elif (USD_avg < float(USD[-1]) and USD_avg_50 > float(USD[-1]) and game_obj.stock_usd != 0):
        print("sell BTC_ETH {}".format(game_obj.stock_usd))
        game_obj.stock_btc += game_obj.stock_usd
        game_obj.stock_usd = 0
    elif (USD_avg > float(USD[-1]) and USD_avg_50 > float(USD[-1]) and game_obj.s_initial_stack > 0):
        print("buy BTC_ETH 0.0001")
        game_obj.stock_usd += 0.0001 * float(game_obj.s_transaction_fee_percent)
        game_obj.s_initial_stack -= 0.0001 * float(USD[-1])
    else:
        print("pass")
