# @author
# Ashutosh.Verma

# Problem: https://leetcode.com/problems/valid-palindrome/

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=[]
        for i in s:
            if i.isalnum():
                a.append(i.lower())  
        x=''.join(a)
        if x==x[::-1]:
            return True
        else:
            return False
        