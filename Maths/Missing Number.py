# @author
# Ashutosh.Verma

# Problem: https://leetcode.com/problems/missing-number/

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x=sum(nums)
        s=(len(nums)*(len(nums)+1))//2
        return s-x
        