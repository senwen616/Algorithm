class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left = 0
        right = 0
        valid = 0
        l = 1000000
        window = {}
        need = {}
        for i in t:
            if i in need:
                need[i] += 1
            else:
                need[i] = 1
        while (right < len(s)):
            c = s[right]
            if c in need:
                if c in window:
                    window[c] += 1
                else:
                    window[c] = 1
                if window[c] == need[c]:
                    valid += 1
            right += 1
            while (valid == len(need)):
                if right - left < l:
                    start = left
                    l = right - left
                c = s[left]
                left += 1
                if c in need:
                    if window[c] == need[c]:
                        valid -= 1
                    window[c] -= 1
        if l == 1000000:
            return ""
        else:
            return s[start: start+l]



if __name__ == '__main__':
    s = Solution()
    print(s.minWindow("ADOBECODEBANC","ABC"))