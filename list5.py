try:
    inputslist=[]
    l=[]
    t='1'# define t to stop the while loop when get -1 as a input
    while t!='-1':
        inputs=input()
        t=inputs
        l=inputs.split()
        for i in range(len(l)):
            l[i]=int(l[i])
        if t!='-1':
            inputslist.append(l)
    length=len(inputslist[0])
    for j in range(len(inputslist)):
        if length==len(inputslist[j]):
            d=2 #difine d to check the invalid matrix
            continue
        else:
            d=1
            print('Invalid Matrix')
            break
    if d!=1:    
        for k in range(len(inputslist[0])):
            for m in range(len(inputslist)):
                print(inputslist[m][k],end=' ')
            print()
except:
    print('error')
               
               
