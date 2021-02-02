#!/bin/python3

import os
import sys

# Complete the solve function below.
def solve(n):
    flag=0
    i=1
    ans=0
    while(flag==0):
        x=bin(i).replace("0b", "") 
        x=x.replace('1','9')
        #print("test",int(x))
        if(int(x)%n==0):
            flag=1
            ans=x
        i=i+1
    return(ans)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = solve(n)

        fptr.write(result + '\n')

    fptr.close()