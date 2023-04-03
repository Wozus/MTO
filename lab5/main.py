#!/usr/bin/env python3

import sys
import re


def change_for_xg(num):
    if num[0] == '-':
        num = num[1:]
    tmp = [int(dec) for dec in num]
    for j in range(len(tmp)):
        tmp[j] = tmp[j] - 1
        if tmp[j] == -1:
            tmp[j] = 9
    return int(''.join(map(str, tmp)))

def my_printf(format_string, param):
    search = re.search("#([1-9]\d*)g", format_string)
    if search is None or not param.isnumeric():
        print(format_string)
        return
    else:
        print_max = int(search.group(1))
        param_len = len(param)
        size = max(0, print_max - param_len)
        flag = param[0] == '-'
        val = change_for_xg(param)

        if flag:
            val = val * -1

        val = (' ' * size) + str(val)
        print(format_string.replace(search.group(0), str(val)))

data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i+1].rstrip())
