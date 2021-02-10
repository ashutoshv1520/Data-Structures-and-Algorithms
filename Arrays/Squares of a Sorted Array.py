# @author
# Ashutosh.Verma

# Problem: https://leetcode.com/problems/squares-of-a-sorted-array/

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        out=[]
        for i in nums:
            out.append(i*i)
        
        out.sort()
        
        return out
        
# use two pointer approach to solve in optimised manner