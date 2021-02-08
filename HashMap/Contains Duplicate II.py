# @author
# Ashutosh.Verma

# Problem: https://leetcode.com/problems/contains-duplicate-ii/

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        d={}
        flag=0
        for i in range(len(nums)):
            if nums[i] in d:
                x=abs(d[nums[i]]-i)
                d[nums[i]]=x
                if x<=k:
                    flag=1
                    break
            else:
                d[nums[i]]=i
        
        if flag==1:
            return True
        else:
            return False
        