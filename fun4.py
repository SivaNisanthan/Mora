date=input()
l=date.split(' ')
y=int(l[0])
m=int(l[1])
d=int(l[2])
if m<3:
    m=m+12
    y=y-1
a = 2*m + int(6*(m + 1) / 10) 
b = y+(int(y/4))-(int(y/100))+(int(y/400))
f1 = d + a + b +1
f = f1 % 7
print(f)
