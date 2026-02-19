class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        p = 0     
        c = 1     
        ans = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                c += 1
            else:
                ans += min(p, c)
                p = c
                c = 1
        ans += min(p, c)
        return ans
        