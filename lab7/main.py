#!/usr/bin/env python3

import sys
import re

change = {
    'a': 'g',
    'b': 'h',
    'c': 'i',
    'd': 'j',
    'e': 'k',
    'f': 'l'
}


def change_16(num):
    tmp = [dec for dec in num]
    for i in range(len(tmp)):
        if change[tmp[i]]:
            tmp[i] = change[tmp[i]]

def my_printf(format_string, param):
    search = re.search("#x", format_string)
    if search is None:
        print(format_string)
        return
    else:
        value_16 = int(param, 16)
        change_16(value_16)
        print(format_string.replace(search.group(0), value_16))

data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i + 1].rstrip())
