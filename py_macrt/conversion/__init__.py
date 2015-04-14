#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""Defines the conversions laws."""


def RuOx(R):
    "Oxford RuOx thermometer."
    import math
    if R > 1e4:
        return 26282.26211 * math.pow(R, -1.182087377)
    return 0.123684 * math.exp(12018.93477 / R) + \
        10379.105 / math.pow(R, 1.25733) - 7.89e-4


def AB(R):
    "Oxford Allen-Bradley thermometer."
    import math
    return 3.60377 * math.exp(1062.013134 / R) + \
        3532.70496 / math.pow(R, 1.07639) + 1513.7033 / R - \
        1.369669
