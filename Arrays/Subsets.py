# @author
# Ashutosh.Verma

# Problem: https://leetcode.com/problems/subsets/

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        q=[[]]
        for i in nums:
            a=[]
            for j in q:
                x=list(j)
                x.append(i)
                a.append(x)
            q.extend(a)
        return q