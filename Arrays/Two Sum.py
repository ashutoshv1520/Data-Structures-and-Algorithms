# @author
# Ashutosh.Verma

# Problem: https://leetcode.com/problems/two-sum/

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        ans=[]
        flag=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    s=(nums[i]+nums[j])
                    if s==target:
                        ans.append(i)
                        ans.append(j)
                        flag=1
                        break
            if flag==1:
                break
        return ans
                                    
