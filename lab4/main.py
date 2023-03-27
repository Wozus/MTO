#!/usr/bin/env python3

import sys
import re

def correct_change(num):
    if int(num) < 0:
        tmp = num[1:]
        return "-" + tmp[::-1]
    return num[::-1]
def my_printf(format_string, param):
    search = re.search("#g", format_string)
    if search is None:
        print(format_string)
        return
    else:
        print(format_string.replace(search.group(0), str(int(correct_change(param)))))

data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i+1].rstrip())
