#!/usr/bin/env python3

import sys

def my_printf(format_string, param):
    print("")

data = sys.stdin.readlines()

for i in range(0, len(data), 2):
    my_printf(data[i].rstrip(), data[i+1].rstrip())
