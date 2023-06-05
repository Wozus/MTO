#!/usr/bin/env python3

import sys
import re

data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']


def change_num(number):
    nums = [dec for dec in str(number)]
    counter = 0
    for i in range(len(nums) - 1, -1, -1):
        if nums[i] == '1':
            nums[i] = data[counter % 10]
        else:
            nums[i] = '0'
        counter += 1
    return ''.join(map(str, nums))
def my_printf(format_string, param):
    search = re.search("#b", format_string)
    if search is None:
        print(format_string)
        return
    num_bin = bin(int(param))
    num_bin = num_bin.lstrip('0')
    res = change_num(num_bin)
    print(res)

# data = sys.stdin.readlines()
#
# for i in range(0, len(data), 2):
#    my_printf(data[i].rstrip(), data[i + 1].rstrip())

my_printf("#b", "123123123")