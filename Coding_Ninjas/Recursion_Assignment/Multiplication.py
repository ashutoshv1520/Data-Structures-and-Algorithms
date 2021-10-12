## Read input as specified in the question.
## Print output as specified in the question.

def mul(m,n):
    if m<n:
        return mul(n,m)
    if n==0:
        return 0
    if m==0:
        return 0
    else:
        return m+mul(m,n-1)

m=int(input())
n=int(input())
print(mul(m,n))

