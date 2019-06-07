#! /usr/bin/env python3

import sys
import utils
from game import GameGraph
from candle import Candle
from action import *

if __name__ == "__main__":
    ## Please don't look at this shet
    game_obj = GameGraph([], "", 0, 0, 0, "", 0, 0, 0, 0, [], [], [], 0, 6)
    for input_line in sys.stdin:
        if (input_line[:8] == "settings"):
            settings_line = input_line.split(' ')
            game_obj[settings_line[1]] = settings_line[2]
        elif (input_line[:24] == "update game next_candles"):
            update_lines = input_line[25:].split(';')
            game_obj.add_new_chart(update_lines)
            utils.eprint(update_lines)
        elif (input_line[:18] == "update game stacks"):
            update_lines = input_line[19:]
            utils.eprint(update_lines)
        elif (input_line[:6] == "action"):
            print("pass")
    utils.eprint("settings: {},updates: {}".format(game_obj.s_player_names, game_obj.game_candles_btc_eth))
