#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

# User input 3 number, sort it and print it
numbers_string = input('Enter 3 numbers use space to seperate it >> ')
sep_numbers = numbers_string.split()
try:
    numbers = [int(n) for n in sep_numbers]
except (ValueError, TypeError) as e:
    print(e)
    sys.exit(1)
else:
    if len(set(numbers)) != 3:
        print('Your input should be 3 digit (no same digit)!')
        sys.exit(1)

# Way1
# Use if clause
copy_numbers = numbers[:]
order = None
a, b, c = copy_numbers
if a > b:
    if b > c:
        order = (c, b, a)
    else:
        if a > c:
            order = (b, c, a)
        else:
            order = (b, a, c)
else:
    if a > c:
        order = (c, a, b)
    else:  # a < c, b > a
        if b > c:
            order = (a, c, b)
        else:  # c > a, b > a, c > b
            order = (a, b, c)

print(order)
# Way2
# Use max() method

# teacher answer
copy_numbers = numbers[:]
new_list = []
while copy_numbers:
    num = max(copy_numbers)
    new_list.insert(0, num)
    copy_numbers.remove(num)
    if len(copy_numbers) == 1:
        new_list.insert(0, copy_numbers[0])
        break

print(new_list)

# my answer
copy_numbers = numbers[:]
the_max = max(copy_numbers)
copy_numbers.remove(the_max)
the_mid = max(copy_numbers)
copy_numbers.remove(the_mid)
copy_numbers.extend([the_mid, the_max])
print(copy_numbers)

# Way3
# Use sort() method
copy_numbers = numbers[:]
copy_numbers.sort()
print(copy_numbers)


# Way4
# Bubble sort
def bubble_sort(nums):
    length = len(nums)

    for i in range(length - 1):
        swapped = False
        for j in range(length - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
                swapped = True
        if not swapped:
            break
    return nums


copy_numbers = [10, 2, 58, 91, 194, 13, 19, 127, 58]
print(bubble_sort(copy_numbers))
