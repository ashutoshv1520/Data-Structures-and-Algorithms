# @author
# Ashutosh.Verma

# Problem: https://leetcode.com/problems/subsets-ii/

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        q=[[]]
        start=0
        end=0
        for i in range(len(nums)):
            start=0
            if i>0 and nums[i]==nums[i-1]:
                start=end+1
            end=len(q)-1
            for j in range(start,end+1):
                x=list(q[j])
                x.append(nums[i])
                q.append(x)
        return q