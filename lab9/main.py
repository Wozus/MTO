#!/usr/bin/env python3

import sys
import re

change = {
    '0': 'a',
    '1': 'b',
    '2': 'c',
    '3': 'd',
    '4': 'e',
    '5': 'f',
    '6': 'g',
    '7': 'h',
    '8': 'i',
    '9': 'j'
}

def change_before(num):
    tmp = [dec for dec in str(num)]
    for iter in range(len(tmp)):
        if change.get(tmp[iter]):
            tmp[iter] = change[tmp[iter]]
    return ''.join(map(str, tmp))

def change_after(num):
    tmp = [dec for dec in str(num)]
    for iter in range(len(tmp)):
        tmp[iter] = str((int(tmp[iter]) + 5) % 10)
    return ''.join(map(str, tmp))

def correct_length(value, length):
    splited = str(value).split('.')
    length_c = max(0, length - len(splited[1]))
    return str(value) + ('0' * length_c)

def my_printf(format_string, param):
    search = re.search("#.([1-9]\d*)h", format_string)
    if search is None:
        print(format_string)
        return

    param_value = float(param)
    format_value = int(search.group(1))
    round_value = round(param_value, ndigits=format_value)

    round_value = correct_length(round_value, format_value).split('.')
    after_first = change_before(round_value[0])
    after_second = change_after(round_value[1])

    print(format_string.replace(search.group(0), after_first + '.' + after_second))



data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i + 1].rstrip())