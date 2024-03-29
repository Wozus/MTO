#!/usr/bin/env python3

import sys
import re

def count_digits(n):
    if n == 0:
        digits = 1
    else:
        digits = len(str(abs(n)))
    return digits


def my_printf(format_string, param):
    search = re.search("#a", format_string)
    if search is None:
        print(format_string)
        return
    digits = count_digits(int(param))
    final = int((int(param) * 2) / digits)

    if final % 2 == 0:
        print(format_string.replace(search.group(0), str(final)))
    else:
        print(format_string.replace(search.group(0), str(hex(final)).replace('0x', '')))

data = sys.stdin.readlines()

for i in range(0, len(data), 2):
   my_printf(data[i].rstrip(), data[i + 1].rstrip())
