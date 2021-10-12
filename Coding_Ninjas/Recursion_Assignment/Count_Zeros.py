## Read input as specified in the question.
## Print output as specified in the question.
def count_zeros(s):
    #print(s,s%10)
    if s==0:
        return 1
    if s<=9:
        return 0
    if 0==s%10:
        return 1+count_zeros(s//10)
    else:
        return count_zeros(s//10)
        
s=int(input())
print(count_zeros(s))