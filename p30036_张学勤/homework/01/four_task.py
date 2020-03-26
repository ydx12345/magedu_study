#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# task1:
# 9 x 9 Multiplication Table


def multiplication_table():
    for i in range(1, 10):
        for j in range(1, i + 1):
            print('{:1} x {:1} = {:<3} '.format(i, j, i * j), end='')
        print(end='\n')


multiplication_table()


# task2:
# print below diamond diagram
#         *
#        ***
#       *****
#     *********
#       *****
#        ***
#         *
def diamond():
    s = '*'
    for i in range(1, 8, 2):
        print((s * i).center(7))
    for i in reversed(range(1, 6, 2)):
        print((s * i).center(7))


diamond()


# task3:
# fibonacci sequence under 100
def fib(number):
    fib_lst = []
    a, b = 1, 1
    while a <= number:
        fib_lst.append(a)
        a, b = b, a + b
    return fib_lst


print(fib(100))


# task4:
# get the specific fibonacci 101 item
def fib2(index):
    a, b = 0, 1
    for i in range(index):
        a, b = b, a + b
    return a


assert fib2(10) == 55


# task5:
# get the prime number under 10000
def prime_numbers(number):
    prime_lst = [2]
    for i in range(3, number):
        for j in range(2, i):
            if i % j == 0:
                break
            else:
                prime_lst.append(i)
    return prime_lst


print(prime_numbers(10000))
