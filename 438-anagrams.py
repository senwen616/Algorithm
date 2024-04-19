class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import defaultdict
        need = defaultdict(int)
        windows = defaultdict(int)
        l = []
        right = 0
        left = 0
        valid = 0
        for c in p:
            need[c] += 1
        while(right < len(s)):
            c = s[right]
            if c in need:
                windows[c] += 1
                if windows[c] == need[c]:
                    valid += 1
            right += 1
            while(right - left >= len(p)):
                c = s[left]
                if valid == len(need):
                    l.append(left)
                if c in need:
                    if windows[c] == need[c]:
                        valid -= 1
                    windows[c] -= 1
                left += 1
        return l

if __name__ == '__main__':
    s = Solution()
    print(s.findAnagrams("cbaebabacd","abc"))