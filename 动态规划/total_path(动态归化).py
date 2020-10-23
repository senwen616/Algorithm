#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: swp
@file: total_pah(动态归化).py
@time:   2020/9/17
@version:  
"""
"""
描述：从上至下，从左往右，走到最后一格的路径总条数
----------
----------
----------
----------
"""


# 利用动态规划，当前格子的路径数来自它的左边和上边

def get_total_path(m, n):
    nums = [1 for _ in range(n)]
    for i in range(m-1):
        for j in range(n):
            if j != 0:
                nums[j] = nums[j - 1] + nums[j]
    return nums


if __name__ == '__main__':
    print(get_total_path(3, 2))
