a1=int(input('Enter angle 1: '))
a2=int(input('Enter angle 2: '))
a3=int(input('Enter angle 3: '))
if a1+a2+a3==180 and a1>0 and a2>0 and a3>0:
    ma=max([a1,a2,a3])
    if ma<90:
        print('Acute angled')
    elif ma==90:
        print('Right angled')
    else:
        print('Obtuse angled')
else:
    print('Angles do not form a triangle')
