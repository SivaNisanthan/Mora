a=input('enter the numbers :- ')
b=a.split()
c=0
for i in b:
    s=bin(int(i))[2:]
    if s.count('1')==1:
        c=c+1
print(c)        
    
