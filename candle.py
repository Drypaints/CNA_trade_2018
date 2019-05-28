#! /usr/bin/env python3

import math

class Candle:
    """
        Class containing data and methods for candlestick chart trading
        Data contained:
          - pair:   The chart to which this candle belongs.
          - date:   Unix timestamp, which represents a certain date and time.
          - high:   The highest price traded in this candle.
          - low:    The lowest price traded in this candle.
          - open:   The opening price of this candle.
          - close:  The closing price of this candle.
          - volume: The total volume that has been traded in this candle.
    """
    def __init__(self, pair, date, high, low, c_open, c_close, volume):
        """
        Constructor method, all data required
        """
        ## Data provided by the program
        self.pair = pair
        self.date = int(date)
        self.high = float(high)
        self.low = float(low)
        self.open = float(c_open)
        self.close = float(c_close)
        self.volume = float(volume)
        ## useful data which can be easily computed during class construction
        ##      The color corresponds to the trend observed during the last candle (green for an increasing price)
        ##      The body is the size of the evolution during this period of time
        ##      The shadows correspond to the highest and lowest prices during this period
        self.color = "green" if self.open < self.close else "red"
        self.body = math.fabs(self.open - self.close)
        self.u_shadow = self.high - (self.close if self.color == "green" else self.open)
        self.l_shadow = (self.open if self.color == "green" else self.close) - self.low
    def is_red(self):
        return self.color == "red"
    def is_green(self):
        return self.color == "green"
