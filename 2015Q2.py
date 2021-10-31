w1=input('enter the 1st word= ')
w2=input('enter the 2nd word= ')
w3=input('enter the 3rd word= ')
l1=list(w1)
l2=list(w2)
l3=list(w3)
if (w1 in w3) and (w2 in w3):
    print('Not Suffle')
else:
    l4=l3[:]
    n1=n2=len(l3)
    for n in l1:
        if n in l3:
            l3.remove(n)
    print(l3)
    for m in l2:
        if m in l4:
            l4.remove(m)
    print(l4)    
    if (len(l1)==n1-len(l3)) and (len(l2)==n2-len(l4)):
        print('Suffle')
    else:
        print('1st two words are not in 3rd word')
    
