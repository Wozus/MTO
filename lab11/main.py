#!/usr/bin/env python3

import sys
import re

data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


def change_num(number):
    if n == 0:
        digits = 1
    else:
        digits = len(str(abs(n)))
    return digits


def my_printf(format_string, param):
    search = re.search("#b", format_string)
    if search is None:
        print(format_string)
        return


data = sys.stdin.readlines()

for i in range(0, len(data), 2):
   my_printf(data[i].rstrip(), data[i + 1].rstrip())
