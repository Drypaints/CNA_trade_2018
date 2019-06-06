#! /usr/bin/env python3

import utils
from candle import Candle

class GameGraph:
    """
    Class containing game-related data and methods
    Used to compute and help decision-making
    Data contained:
      - settings-related data:
        - player_names:            [Str]
        - your_bot:                Str
        - timebank:                Int
        - time_per_move:           Int
        - candle_interval:         Int
        - candle_format:           Str
        - candles_total:           Int
        - candles_given:           Int
        - initial_stack:           Float
        - transaction_fee_percent: Float
      - game_candles*:              [Candle]
      - game_stacks:               Float
    """
    def __init__(self, player_names, your_bot, timebank, time_per_move, candle_interval, candle_format, candles_total, candles_given, initial_stack, transaction_fee_percent, game_candles_btc_usdt, game_candles_btc_eth, game_candles_eth_usdt, game_stacks, period):
        """
        Constructor method, all data required
        """
        self.s_player_names = player_names
        self.s_your_bot = your_bot
        self.s_timebank = timebank
        self.s_time_per_move = time_per_move
        self.s_candle_interval = candle_interval
        self.s_candle_format = candle_format
        self.s_candles_total = candles_total
        self.s_candles_given = candles_given
        self.s_initial_stack = initial_stack
        self.s_transaction_fee_percent = transaction_fee_percent
        self.game_candles_btc_eth = game_candles_btc_eth
        self.game_candles_eth_usdt = game_candles_eth_usdt
        self.game_candles_btc_usdt = game_candles_btc_usdt
        self.game_stacks = game_stacks
        self.relative_evo = []
        self.std_deviation = []
        self.increase_avg = []
    def __getitem__(self, name):
        if name == "player_names":
            return self.s_player_names
        elif name == "your_bot":
            return self.s_your_bot
        elif name == "timebank":
            return self.s_timebank
        elif name == "time_per_move":
            return self.s_time_per_move
        elif name == "candle_interval":
            return self.s_candle_interval
        elif name == "candle_format":
            return self.s_candle_format
        elif name == "candles_total":
            return self.s_candles_total
        elif name == "candles_given":
            return self.s_candles_given
        elif name == "initial_stack":
            return self.s_initial_stack
        elif name == "transaction_fee_percent":
            return self.s_transaction_fee_percent
        elif name == "game_candles_btc_eth":
            return self.game_candles_btc_eth
        elif name == "game_candles_eth_usdt":
            return self.game_candles_eth_usdt
        elif name == "game_candles_btc_usdt":
            return self.game_candles_btc_usdt
        elif name == "game_stacks":
            return self.game_stacks
        else:
            utils.eprint("Error: name {} doesn't exist".format(name))
            raise IndexError
    def __setitem__(self, name, value):
        if name == "player_names":
            self.s_player_names = value.rstrip("\n\r").split(',')
        elif name == "your_bot":
            self.s_your_bot = value
        elif name == "timebank":
            self.s_timebank = value
        elif name == "time_per_move":
            self.s_time_per_move = value
        elif name == "candle_interval":
            self.s_candle_interval = value
        elif name == "candle_format":
            self.s_candle_format = value
        elif name == "candles_total":
            self.s_candles_total = value
        elif name == "candles_given":
            self.s_candles_given = value
        elif name == "initial_stack":
            self.s_initial_stack = value
        elif name == "transaction_fee_percent":
            self.s_transaction_fee_percent = value
        elif name == "game_candles_btc_eth":
            self.game_candles_btc_eth = value
        elif name == "game_candles_eth_usdt":
            self.game_candles_eth_usdt = value
        elif name == "game_candles_btc_usdt":
            self.game_candles_btc_usdt = value
        elif name == "game_stacks":
            self.game_stacks = value
        else:
            utils.eprint("Error: name {} doesn't exist".format(name))
            raise IndexError
    ## and self.game_candles[-1].volume >= self.game_candles[-2].volume ## à tester
    # def is_hammer_candlestick(self):
    #     if (len(self.game_candles) > 3 and self.game_candles[-2].is_red() and self.game_candles[-3].is_red() and self.game_candles[-4].is_red()
    #         and self.game_candles[-1].is_green() and self.game_candles[-1].l_shadow > self.game_candles[-1].body * 2):
    #         return True
    #     else:
    #         return False
    # ## and self.game_candles[-1].volume >= self.game_candles[-2].volume ## à tester
    # def is_shooting_star_candlestick(self):
    #     if (len(self.game_candles) > 3 and self.game_candles[-2].is_green() and self.game_candles[-3].is_green() and self.game_candles[-4].is_green()
    #         and self.game_candles[-1].is_red() and self.game_candles[-1].u_shadow > self.game_candles[-1].body * 2):
    #         return True
    #     else:
    #         return False
    # ## made to detect a trend change and trigger short-sell or short buy
    # def is_doji_candlestick(self):
    #     if (len(self.game_candles) >= 1
    #         and self.game_candles[-1].body * 5 < self.game_candles[-1].l_shadow
    #         and self.game_candles[-1].body * 5 < self.game_candles[-1].u_shadow):
    #         return True
    #     else:
    #         return False
    def add_new_chart(self, data):
        for elt in data:
            if (elt[:7] == "btc_eth"):
                self["game_candles_" + elt[:7].lower()] = elt
            else:
                self["game_candles_" + elt[:8].lower()] = elt
            utils.eprint("game_candles_" + elt[:7].lower())
        utils.eprint(">>> New input :", data, '\n')
