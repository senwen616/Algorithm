#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: swp
@file: 651_四键键盘.py
@time:   2020/11/6
@version:  
"""


def get_max(n):
    dp = [None] * (n+1)
    dp[0] = 0
    for i in range(1, n+1):
        dp[i] = dp[i - 1] + 1
        for j in range(2, i):
            dp[i] = max(dp[i], dp[j - 2] * (i - j + 1))
    return dp[n]


if __name__ == '__main__':
    print(get_max(15))
