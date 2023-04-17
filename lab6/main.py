#!/usr/bin/env python3

import sys
import re


def change_for_xg(num):
    if num[0] == '-':
        num = num[1:]
    tmp = [int(dec) for dec in num]
    for iter in range(len(tmp)):
        tmp[iter] = (tmp[iter] * 9 + 1) % 10
    return ''.join(map(str, tmp))

def my_printf(format_string, param):
    search = re.search("#.([1-9]\d*)g", format_string)
    if search is None:
        print(format_string)
        return
    else:
        print_max = int(search.group(1))
        flag = param[0] == '-'
        val = change_for_xg(param)
        param_len = len(val)
        size = max(0, print_max - param_len)
        val = ('0' * size) + str(val)
        if flag:
            val = '-' + val
        print(format_string.replace(search.group(0), val))

data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i+1].rstrip())
