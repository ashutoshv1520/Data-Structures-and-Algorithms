# @author
# Ashutosh.Verma

# Problem: https://leetcode.com/problems/contains-duplicate/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d={}
        for i in nums:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        flag=0        
        for i in d:
            if d[i]>1:
                flag=1
        if flag==1:
            return True
        else:
            return False