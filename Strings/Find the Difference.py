# @author
# Ashutosh.Verma

# Problem: https://leetcode.com/problems/find-the-difference/

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        x=s+t
        d={}
        for i in x:
            if i in d:
                d[i]=d[i]+1
            else:
                d[i]=1
        
        ans=""
        for i in d:
            if d[i]%2!=0:
                ans=i
                break
        return ans
            