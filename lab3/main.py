#!/usr/bin/env python3

import sys
import re

def my_printf(format_string, param):
    search_group = re.search("#(\d*)?(\.\d*)?k", format_string)
    if search_group is None:
        print(format_string)
    else:
        swap_param = param.swapcase()
        to_print = search_group.group(0)
        min_length = search_group.group(1)
        max_length = search_group.group(2)

        if min_length is not None and min_length.isnumeric():
            min_value = int(min_length)
            if min_value > 0:
                swap_param += ' ' * (min_value - len(swap_param))

        if max_length is not None and max_length.isnumeric():
            max_value = int(max_length[1:])
            if max_value > 0:
                swap_param = swap_param[:min(max_value, len(swap_param))]

        print(format_string.replace(to_print, swap_param))

data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i+1].rstrip())
