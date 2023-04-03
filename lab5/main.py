#!/usr/bin/env python3

import sys
import re


def change_for_xg(num):
    tmp = [int(dec) for dec in num]
    for j in range(len(tmp)):
        tmp[j] = tmp[j] - 1
        if tmp[j] == -1:
            tmp[j] = 9
    return int(''.join(map(str, tmp)))

def my_printf(format_string, param):
    search = re.search("#([1-9]\d*)g", format_string)
    if search is None or param.isnumeric():
        print(format_string)
        return
    else:
        print(format_string.replace(search.group(0), str(change_for_xg(param))))

data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i+1].rstrip())
