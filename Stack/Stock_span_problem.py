#User function Template for python3


class Solution:
    
    #Function to calculate the span of stockâ€™s price for all n days.
    def calculateSpan(self,a,n):
        #code here
        s=[]
        v=[]
        for i in range(n):
            while(len(s)!=0 and s[-1][0]<=a[i]):
                s.pop()
            if len(s)==0:
                v.append(-1)
            else:
                v.append(s[-1][1])
            s.append([a[i],i])
        #print(v)
        
        res=[]
        for i in range(len(v)):
            res.append(i-v[i])
        
        return res
