## Read input as specified in the question.
## Print output as specified in the question.
def strint(s):
    print(s)
    if len(s)==1:
        return s
    if s[0]=='0':
        return strint(s[1:])
    else:
        return s[0]+strint(s[1:])
s=int(input())
print(s)

#strint(s)
