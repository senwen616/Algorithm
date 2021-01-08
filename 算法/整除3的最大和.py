#!/usr/bin/python
# -* - coding: UTF-8 -* -
"""
给你一个整数数组 nums，请你找出并返回能被三整除的元素最大和。
示例 1：

输入：nums = [3,6,5,1,8]
输出：18
解释：选出数字 3, 6, 1 和 8，它们的和是 18（可被 3 整除的最大和）。
"""
class Solution(object):
    def max_sum3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0, 0, 0]
        l = len(nums)
        for i in range(l):
            mod = nums[i] % 3
            a = dp[(3 + 0 - mod) % 3]
            b = dp[(3 + 1 - mod) % 3]
            c = dp[(3 + 2 - mod) % 3]
            if a or mod == 0:
                dp[0] = max(dp[0], a + nums[i])
            if b or mod == 1:
                dp[1] = max(dp[1], b + nums[i])
            if c or mod == 2:
                dp[2] = max(dp[2], c + nums[i])
        return dp[0]


if __name__ == '__main__':
    nums = [1, 5, 6, 3, 4]
    solution = Solution()
    print solution.max_sum3(nums)

