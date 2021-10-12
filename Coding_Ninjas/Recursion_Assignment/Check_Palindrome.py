## Read input as specified in the question.
## Print output as specified in the question.
def check_palin(s):
    if len(s)==0 or len(s)==1:
        return "true"
    elif s[0]==s[-1]:
        return check_palin(s[1:-1])
    else:
        return "false"

s=input()
print(check_palin(s))