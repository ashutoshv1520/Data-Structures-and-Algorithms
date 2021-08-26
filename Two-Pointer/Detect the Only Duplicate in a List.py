# https://binarysearch.com/problems/Detect-the-Only-Duplicate-in-a-List

# using dictionary
# should use hare and tortise

class Solution:
    def solve(self, nums):
        d={}
        x=""
        for i in nums:
            if i in d:
                x=i
                break
            else:
                d[i]=1
        #print(d)
        return x
        