## Read input as specified in the question.
## Print output as specified in the question.
def lastIndex(arr,x,si):
    l=len(arr)
    if si==l:
        return -1
    smallerListOutput=lastIndex(arr,x,si+1)
    if smallerListOutput!=-1:
    	return smallerListOutput
    else:
    	if arr[si]==x:
    		return si
    	else:
        	return -1
        
    
    
    


n=int(input())
arr=list(map(int,input().split()))
x=int(input())
si=0
print(lastIndex(arr,x,si))