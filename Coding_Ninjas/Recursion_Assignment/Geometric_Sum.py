## Read input as specified in the question.
## Print output as specified in the question.
def gsum(k):
    if k==0:
        return 1
    else:
        #print((1/(2**k)),k)
        return (1/(2**k))+gsum(k-1)


k=int(input())
x="{0:.5f}"
print(x.format(gsum(k)))