n=int(input('Input number: '))
t2=0
if n>1:
    for i in range(2,n+1):
        d=1
        t1=0
        while i//d>1:
            if i%d==0:
                t1=t1+d
                d=d+1
            else:
                d=d+1
        if t1>i:
            t2=t2+1
    print('Number of abundant numbers from 1 to',n,'is',t2)
else:
    print('Invalid Input')
