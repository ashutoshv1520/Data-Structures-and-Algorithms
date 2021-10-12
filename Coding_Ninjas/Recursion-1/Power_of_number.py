## Write your code here
## To take space separated input for two variables, we use the following syntax (3 lines)

def power(x,n):
    
    if n==0:
        return 1
    else:
        return x*power(x,n-1)






a, b = input().split()
x = int(a)
n = int(b)

print(power(x,n))
























