#!/usr/bin/env python3

import sys
import re

def my_printf(format_string, param):
    match = re.search("#(\.\d*)?k", format_string)
    if match is None:
        match = re.search("#k", format_string)
        replacement = format_string[match.start():match.end()]
        print(format_string.replace(replacement, param.swapcase()), end="")
    else:
        replacement = format_string[match.start():match.end()]
        max_chars = len(param)
        if match.group(1):
            max_chars = int(replacement[2:-1])

        print(format_string.replace(replacement, param[0: max_chars].swapcase()), end="")
    print("")

data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i+1].rstrip())
