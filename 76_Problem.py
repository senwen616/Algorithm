class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import defaultdict
        need = defaultdict(int)
        windows = defaultdict(int)
        for c in t:
            need[c] += 1
        fast = 0
        slow = 0
        value = 0
        l = float("inf")
        while fast < len(s):
            c = s[fast]
            if c in need:
                # windows[c] + 1  # here
                windows[c] += 1
                if windows[c] == need[c]:
                    value += 1
            fast += 1
            while value == len(need):
                if fast - slow < l:
                    l = fast - slow
                    start = slow
                c = s[slow]
                if c in need:

                    if windows[c] == need[c]:
                        value -= 1
                    windows[c] -= 1
                slow += 1
        if l != float("inf"):
            # return s[start,start + l]  # !here
            return s[start:start + l]  # !here
        else:
            return ""


if __name__ == '__main__':
    s = Solution()
    print(s.minWindow("ADOBECODEBANC", "ABC"))
