# @author
# Ashutosh.Verma

# Problem: https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        ws=0
        d={}
        maxL=0
        
        for we in range(len(s)):
            char = s[we]
            if char in d:
                ws=max(ws,d[char]+1)
            d[char]=we
            maxL=max(maxL,we-ws+1)
        return maxL
        