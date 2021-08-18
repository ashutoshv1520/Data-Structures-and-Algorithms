#User function Template for python3


class Solution:
    def nextLargerElement(self,arr,n):
        #code here
        stack=[]
        res=[]
        for i in range(n-1,-1,-1):
            while(len(stack)!=0 and stack[-1]<=arr[i]):
                stack.pop()
            if len(stack)==0:
                res.append(-1)
            else:
                res.append(stack[-1])
            stack.append(arr[i])
        return res[::-1]
