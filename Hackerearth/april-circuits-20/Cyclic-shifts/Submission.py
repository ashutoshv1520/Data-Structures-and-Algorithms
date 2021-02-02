t=int(input())
while(t!=0):
    x=input().split(" ")
    n=int(x[0])
    m=int(x[1])
    a=x[2]
    #print(n,m,a)
    y=bin(n).replace('0b','')
    n1=16-len(y)
    z1=n1*"0"+y
    z=[]
    for i in range(len(z1)):
        z.append((z1[i]))
    #print(y)
    #print(z,z1)
    if a=='L':
        temp=0
        for i in range(m):
            al=z[1:]
            al.extend(z[0:1])
            #print(al)
            z=al
            #print(z)
        print(int(''.join(z),2))
    elif a=='R':
        temp=0
        for i in range(m):
            al=z[-1:]
            al.extend(z[0:len(z)-1])
            #print(al)
            z=al
            #print(z)
        print(int(''.join(z),2))
    t=t-1