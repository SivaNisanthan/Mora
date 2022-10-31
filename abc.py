n=int(input())
d=2
while n>0:
    if n==1:
        print('non-prime')
    else:
        while d<n :
            if n%d==0:
                print('non-prime')
                break
            else:
                d=d+1
        if d==n:
            print('prime') 
    n=int(input())
    d=2
