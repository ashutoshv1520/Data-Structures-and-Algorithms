''' Read input from STDIN. Print your output to STDOUT '''
#Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
# Write code here
    t=int(input())
    while(t!=0):
        n=int(input())
        g=input().strip()
        h=input().strip()
        a=list(map(int,g.split(" ")))
        b=list(map(int,h.split(" ")))
        #print(n,a,b,g,h)
        a.sort()
        b.sort()
        #print(a)
        #print(b)
        c=[]
        j=0
        count=0
        for i in range(len(a)):
            if(a[i]>b[j]):
                j=j+1
                count=count+1
        print(count)
        t=t-1                    
main()



