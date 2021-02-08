# @author
# Ashutosh.Verma

# Problem: https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3631/

class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        x=[]
        for i in range(len(s)):
            if s[i]==c:
                x.append(i)
        
        ans=[]
        for i in range(len(x)):
            y=x[i]
            a=[]
            for j in range(len(s)):
                a.append(abs(y-j))
            ans.append(a)
        
        a=list(zip(*ans))
        
        
        b=[]
        for i in a:
            b.append(min(i))
        
        return b
                
            
        
        
                