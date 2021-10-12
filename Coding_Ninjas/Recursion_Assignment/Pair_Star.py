## Read input as specified in the question.
## Print output as specified in the question.
def pairstar(s,si):
    #print(s)
    if len(s)==si or len(s)-1==si:
        return s[si]
    if s[si]==s[si+1]:
        return s[si]+"*"+pairstar(s,si+1)
    else:
        return s[si]+pairstar(s,si+1)
s=input()
print(pairstar(s,0))
