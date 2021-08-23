# binarysearch.com weekly contest 2 

class Solution:
    def solve(self, words):
        c=1
        if len(words)==0:
            return 0
        elif len(words)==1:
            return 1
              
        a=[]
        for i in range(len(words)-1):
            if words[i][0]==words[i+1][0]:
                c=c+1
            else:
                a.append(c)
                c=1
        a.append(c)

        return max(a)

        