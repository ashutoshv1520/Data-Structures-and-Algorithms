''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    
 # Write code here 
    n=int(input())
    x=list(map(str,input().split(" ")))
    y=list(map(str,input().split(" ")))
    a=[]
    for i in range(len(x)-1):
        a.append(int(x[i]))
    b=[]
    for i in range(len(y)):
        b.append(int(y[i]))
    print(n,a,b,x,y)
    m=999999999
    for i in range(len(a)):
        s=b[i]//a[i]
        if s<m:
            m=s
    print(m)
main()


