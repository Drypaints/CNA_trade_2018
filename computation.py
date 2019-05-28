#! /usr/bin/env python3

from math import sqrt

def compute_relative_evo(period = 0, input_list = []):
    if (len(input_list) > period):
        try:
            value = round((input_list[-1] / input_list[-(1 + period)] - 1) * 100)
            return '{}'.format(value)
        except (ValueError, FloatingPointError, ZeroDivisionError):
            return "nan"
    return "nan"

def compute_std_deviation(period = 0, input_list = []):
    if (len(input_list) >= period):
        try:
            avg = sum(input_list[-period:]) / period
            std_dev = sqrt(sum(map(lambda x:(x - avg)**2, input_list[-period:])) / period)
            return '{:.2f}'.format(std_dev)
        except (ValueError, FloatingPointError, ZeroDivisionError):
            return "nan"
    return "nan"

def compute_increase_avg(period = 0, input_list = []):
    if (len(input_list) > period):
        try:
            avg_inc = sum(list(map(lambda x, y: x - y, input_list[-period:], input_list[-(period + 1):-1]))) / period
            return '{:.2f}'.format(avg_inc)
        except (ValueError, FloatingPointError, ZeroDivisionError):
            return "nan"
    return "nan"
