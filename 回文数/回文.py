#!/usr/bin/python
# -* - coding: UTF-8 -* -


class Solution(object):
    def isP(self, s):
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        return True

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l = 0
        r = len(s) - 1
        while l < r:
            if s[l] != s[r]:

                return self.isP(s[l + 1:r+1]) or self.isP(s[l:r])
            else:
                l += 1
                r -= 1
        return True
if __name__ == '__main__':

    so = Solution()
    print(so.validPalindrome("aydmda"))

