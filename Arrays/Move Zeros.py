# @author
# Ashutosh.Verma

# Problem: https://leetcode.com/problems/move-zeroes/

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        x=nums.count(0)
        for i in range(x):
            nums.remove(0)
            nums.append(0)