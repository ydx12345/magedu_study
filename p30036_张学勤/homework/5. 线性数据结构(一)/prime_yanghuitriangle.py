#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# task1
# find the prime number under 100
# if n is composite number, it should have two divisor p1 & p2
# p1 <= sqrt(n), p2 >= sqrt(n)
# [判断 N 是否是质数，为什么判断到根号 N 就可以了？](https://www.zhihu.com/question/21808179)
# [if statement - Why does python use 'else' after for and while loops? - Stack Overflow]
# (https://stackoverflow.com/q/9979970/8057310)
import math

# def sqrt_get_prime():
#     # for ... else version
#     primes = []
#     for i in range(2, 100):
#         for j in range(2, int(math.sqrt(i)) + 1):
#             if i % j == 0:
#                 break
#         else:
#             primes.append(i)
#     return primes


def sqrt_get_prime():
    # for ... if version
    primes = []
    for i in range(2, 100):
        is_prime = True
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes


print(sqrt_get_prime())


# task2
# 6 row of yanghui triangle
def yanghui(times):
    triangle = []
    triangles = []
    for i in range(times):
        if i < 2:
            triangle.append(1)
        else:
            mid_tri = []
            for i in range(len(triangle) - 1):
                mid_tri.append(triangle[i] + triangle[i + 1])
            triangle = [1] + mid_tri + [1]
        triangles.append(tuple(triangle))
    return triangles


print(yanghui(6))
