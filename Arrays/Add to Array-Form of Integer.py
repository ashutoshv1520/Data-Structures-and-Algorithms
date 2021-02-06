# @author
# Ashutosh.Verma

# Problem: https://leetcode.com/problems/add-to-array-form-of-integer/

class Solution(object):
    def addToArrayForm(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: List[int]
        """
        digits=A
        digits=list(map(str,digits))
        x=str(int(''.join(digits))+K)
        ans=[]
        for i in x:
            ans.append(int(i))
        return(ans)
        