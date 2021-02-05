# @author
# Ashutosh.Verma

# Problem: https://leetcode.com/problems/search-insert-position/

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.append(target)
        nums.sort()
        x=nums.index(target)
    
        return(x)
        
        
        