## Read input as specified in the question.
## Print output as specified in the question.
def sum_of_digits(s):
    if len(s)==1:
        return int(s[0])
    else:
        return int(s[0])+sum_of_digits(s[1:])
    

s=input()
print(sum_of_digits(s))
