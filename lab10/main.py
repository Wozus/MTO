#!/usr/bin/env python3

import sys
import re



def my_printf(format_string, param):
    search = re.search("#a", format_string)
    if search is None:
        print(format_string)
        return
    count_digits = len(param)
    final = int((int(param) * 2)/count_digits)





data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i + 1].rstrip())