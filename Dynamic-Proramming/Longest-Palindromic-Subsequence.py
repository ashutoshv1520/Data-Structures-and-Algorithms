# @author
# Ashutosh.Verma

# Problem:

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        X = s
        Y = s[::-1]
        m = len(X)
        n = len(Y)
        arr = []
        
        for i in range(m+1):
            arr.append([0]*(n+1))
        
        for i in range(m+1):
            for j in range(n+1):
                if i == 0 or j == 0 :
                    arr[i][j] = 0
                elif X[i-1] == Y[j-1]:
                    arr[i][j] = 1 + arr[i-1][j-1]
                else:
                    arr[i][j] = max(arr[i-1][j], arr[i][j-1])
        
        return arr[m][n]
        