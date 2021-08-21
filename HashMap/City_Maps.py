# binarysearch.com weekly contest1
class Solution:
    def solve(self, matrix, blocks):
        #print(matrix)
        d={'start':(0,0)}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                d[matrix[i][j]]=(i,j)
        #print(arr)
        s=0
        blocks=["start"]+blocks
        for i in range(len(blocks)-1):
            x=d[blocks[i]]
            y=d[blocks[i+1]]
            s=s+ abs(x[0]-y[0]) +abs(x[1]-y[1])
        
        return s