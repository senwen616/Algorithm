#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: swp
@file: 877石子游戏.py
@time:   2020/12/17
@version:  
"""

"""亚历克斯和李用几堆石子在做游戏。偶数堆石子排成一行，每堆都有正整数颗石子 piles[i] 。

游戏以谁手中的石子最多来决出胜负。石子的总数是奇数，所以没有平局。

亚历克斯和李轮流进行，亚历克斯先开始。 每回合，玩家从行的开始或结束处取走整堆石头。 这种情况一直持续到没有更多的石子堆为止，此时手中石子最多的玩家获胜。

假设亚历克斯和李都发挥出最佳水平，当亚历克斯赢得比赛时返回 true ，当李赢得比赛时返回 false 。

 

示例：

输入：[5,3,4,5]
输出：true
解释：
亚历克斯先开始，只能拿前 5 颗或后 5 颗石子 。
假设他取了前 5 颗，这一行就变成了 [3,4,5] 。
如果李拿走前 3 颗，那么剩下的是 [4,5]，亚历克斯拿走后 5 颗赢得 10 分。
如果李拿走后 5 颗，那么剩下的是 [3,4]，亚历克斯拿走后 4 颗赢得 9 分。
这表明，取前 5 颗石子对亚历克斯来说是一个胜利的举动，所以我们返回 true 。
 

提示：

2 <= piles.length <= 500
piles.length 是偶数。
1 <= piles[i] <= 500
sum(piles) 是奇数。

"""

#  初始化dp数组，每个元组第一维为先手获得的石子数，第二维为后手获得的;
# dp[i][j]表示从第i堆到第j堆石头，如[5,3,4,5]，dp[0][1]表示石头堆[5.3],所以当i和j相等时，先手获得全部，后手为0

import numpy as np


def who_win(piles):
    # 初始化dp
    dp = [[[0, 0] for _ in range(len(piles))] for _ in range(len(piles))]

    # base情况
    for i in range(len(piles)):
        for j in range(i, len(piles)):
            if i == j:
                dp[i][j][0] = piles[i]
                dp[i][j][1] = 0
    # 斜着遍历dp
    for l in range(2, len(piles) + 1):
        for i in range(0, len(piles) - l + 1):
            j = i + l - 1
            # 先手选左右
            left = piles[i] + dp[i + 1][j][1]
            right = piles[j] + dp[i][j - 1][1]
            if left > right:
                dp[i][j][0] = left
                dp[i][j][1] = dp[i + 1][j][0]
            else:
                dp[i][j][0] = right
                dp[i][j][1] = dp[i][j - 1][0]
            print(i, j)
    if dp[0][len(piles) - 1][0] > dp[0][len(piles) - 1][1]:
        print("先手胜")
    print(np.asarray(dp))


if __name__ == '__main__':
    who_win([1, 2, 3, 4])
