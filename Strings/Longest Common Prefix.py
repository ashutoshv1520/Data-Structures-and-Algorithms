# @author
# Ashutosh.Verma

# Problem: https://leetcode.com/problems/longest-common-prefix/

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        b=[]
        for i in range(len(strs)):
            b.append(len(strs[i]))
        if strs==[]:
            n=0
        else:
            n=min(b)
        
        a=[]
        ans=[]
        flag=0
        for j in range(n):
            for i in range(len(strs)):
                a.append(strs[i][j])
            print(a)
            s=list(set(a))
            if len(s)==1:
                ans.append(a[0])
                a=[]
            else:
                flag=1
                a=[]
                break
            if flag==1:
                break
        return(''.join(ans))
            
            