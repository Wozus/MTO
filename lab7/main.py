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
    tmp = [dec for dec in str(num)]
    for iter in range(len(tmp)):
        if change.get(tmp[iter]):
            tmp[iter] = change[tmp[iter]]
    return ''.join(map(str, tmp))

def my_printf(format_string, param):
    search = re.search("#j", format_string)
    if search is None:
        print(format_string)
        return
    else:
        value = int(param)
        value_16 = hex(value)
        result = change_16(value_16)
        print(format_string.replace(search.group(0), result))

data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i + 1].rstrip())
