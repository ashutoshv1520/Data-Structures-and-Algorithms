input=list(map(int,input().split()))
stack=[]
res=[]
for i in range(len(input)):
    while len(stack)!=0 and stack[-1]<input[i]:
        stack.pop()
    if len(stack)==0:
        res.append(-1)
    else:
        res.append(stack[-1])
    stack.append(input[i])
print(res)
