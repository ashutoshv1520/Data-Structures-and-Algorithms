# @author
# Ashutosh.Verma

# Problem: https://leetcode.com/problems/valid-parentheses/

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a=[]
        for i in s:
            a.append(i)

        
        if len(a)==1:
            return False
        
        flag=0
        b=[]
        for i in a:
            if i=='(':
                b.append('(')
            elif i=='[':
                b.append('[')
            elif i=='{':
                b.append('{')
            elif i==')' and len(b)>0 and b[-1]=='(':
                b.pop()
            elif i==']' and len(b)>0 and b[-1]=='[':
                b.pop()
            elif i=='}' and len(b)>0 and b[-1]=='{':
                b.pop()
            elif i==')' or i==']' or i=='}':
                flag=1
                break
            
        
        if flag==1:
            return False
        if len(b)==0:
            return True
            