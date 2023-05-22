#!/usr/bin/env python3

import sys
import re

change = {
    'a': 'g',
    'b': 'h',
    'c': 'i',
    'd': 'j',
    'e': 'k',
    'f': 'l',
    '0': 'o'
}

def change_16(num):
    tmp = [dec for dec in str(num)]
    for iter in range(len(tmp)):
        if change.get(tmp[iter]):
            tmp[iter] = change[tmp[iter]]
    return ''.join(map(str, tmp))

def my_printf(format_string, param):
    search = re.search("#.([1-9]\d*)j", format_string)
    if search is None:
        print(format_string)
        return
    else:
        if param.isnumeric() and search.group(1).isnumeric() and int(search.group(1)) >= 0:
            value = int(param)
            value_16 = hex(value)
            value_16_str = str(value_16)[2:]
            print_max = int(search.group(1))
            param_len = len(param)

            size = max(0, print_max - param_len)
            value_16_str = '0' * size + value_16_str

            result = change_16(value_16_str)
            print(format_string.replace(search.group(0), result))
        else:
            print(format_string)
            return

data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i + 1].rstrip())
