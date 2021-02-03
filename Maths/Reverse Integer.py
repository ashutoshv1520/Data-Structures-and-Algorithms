# @author
# Ashutosh.Verma

# Problem: https://leetcode.com/problems/reverse-integer/

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x>=0:
            s=str(x)
            s=int(s[::-1])
            if s>(2**31):
                return 0
            else:
                return(s)
        else:
            x=-(x)
            s=str(x)
            s=int(s[::-1])
            s=-(s)
            if s<(-2**31):
                return 0
            else:
                return(s)
            
        
        