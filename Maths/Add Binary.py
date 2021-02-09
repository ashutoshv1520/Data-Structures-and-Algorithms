# @author
# Ashutosh.Verma

# Problem: https://leetcode.com/problems/add-binary/

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        
        x=int(a,2)
        y=int(b,2)
        z=x+y
        c=bin(z)
        return c[2:]
        
                