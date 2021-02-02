# @author
# Ashutosh.Verma

# Problem: https://leetcode.com/problems/find-the-most-competitive-subsequence/

class Solution(object):
    def mostCompetitive(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        s = []
        
        for i in range(len(nums)):
            while(len(s)!=0 and nums[i]<s[-1] and len(s)+n-i>k):
                s.pop()
            if len(s)<k:
                s.append(nums[i])
        
        return s
        