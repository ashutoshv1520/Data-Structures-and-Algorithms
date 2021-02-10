# @author
# Ashutosh.Verma

# Problem: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        if len(nums)<=1:
            return len(nums)
        while(True):
            if nums.count(nums[i])>2:
                nums.remove(nums[i])
            else:
                i=i+1
                
            if i==len(nums)-1:
                break
        
        return len(nums)

# use two pointer approach for optimised solution