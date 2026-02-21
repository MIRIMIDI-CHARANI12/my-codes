class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left=0
        ml=0
        chset=set()
        for r in range(len(s)):
            if s[r] not in chset:
                chset.add(s[r])
                ml=max(ml,r-left+1)
            else:
                while s[r] in chset:
                    chset.remove(s[left])
                    left+=1
                chset.add(s[r])
        return ml
        