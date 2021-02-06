# @author
# Ashutosh.Verma

# Problem: https://leetcode.com/problems/plus-one/

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits=list(map(str,digits))
        x=str(int(''.join(digits))+1)
        ans=[]
        for i in x:
            ans.append(int(i))
        while len(ans)<len(digits):
            ans=[0]+ans
        return(ans)
        