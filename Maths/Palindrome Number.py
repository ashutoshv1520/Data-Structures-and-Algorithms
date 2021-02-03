# @author
# Ashutosh.Verma

# Problem: https://leetcode.com/problems/palindrome-number/

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=str(x)
        y=s[::-1]
        if s==y:
            return True
        else:
            return False
        
        