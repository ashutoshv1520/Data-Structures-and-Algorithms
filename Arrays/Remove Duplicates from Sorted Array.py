# @author
# Ashutosh.Verma

# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < (len(nums)-1):
            if nums[i] == nums[i+1]:
                nums.remove(nums[i])
            else:
                i += 1
        return len(nums) 