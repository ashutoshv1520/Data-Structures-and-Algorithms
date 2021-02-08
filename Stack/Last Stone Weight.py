# @author
# Ashutosh.Verma

# Problem: https://leetcode.com/problems/last-stone-weight/

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        while(len(stones)>1):
            stones.sort()
            x=stones.pop()
            y=stones.pop()
            if x==y:
                pass
            elif x!=y:
                stones.append(abs(y-x))
       
        if len(stones)==0:
            return 0
        else:
            return stones[0]
            
        