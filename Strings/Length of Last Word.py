# @author
# Ashutosh.Verma

# Problem: https://leetcode.com/problems/length-of-last-word/

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip()
        if s=='':
            return 0
        a=s.split()
        x=a[-1]
        return len(x)