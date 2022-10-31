try:
    A=input('Enter the dimension: ')#enter the amount of row and column
    def matrix(M):
        global A
        global code
        A1=A.split(',')
        Amatrix=[]
        print('Enter Matrix '+M+':')
        for i in range(int(A1[0])):
            A2=input() #enter the rows of the matrix
            A2=A2.split()
            if len(A2)==int(A1[1]):
                code='nothing'
                for k in range(len(A2)):
                    A2[k]=int(A2[k])
            else:
                print('invalid matrix')
                code='break'
                break
            Amatrix.append(A2)    
        return Amatrix
    def transposematrix(Mlist):
        Tlist=[]
        for i in range(len(Mlist[0])):
            Tlist2=[]
            for j in range(len(Mlist)):
                Tlist2.append(Mlist[j][i])
            Tlist.append(Tlist2)
        return Tlist

    matrixA=matrix('A')
    if code=='nothing':    
        matrixB=matrix('B')
        if code=='nothing':
            TmatrixB=transposematrix(matrixB)
            list1=[]
            for m in range(len(matrixA)):
                l=[]
                for i in range(len(matrixA)):
                    t=0
                    for j in range(len(matrixA[0])):
                        t=t+(matrixA[m][j]*TmatrixB[j][i])
                    l.append(t)
                list1.append(l)
            for n in range(len(list1)):
                for p in range(len(list1[0])):
                    print(list1[n][p],end=' ')
                print()
except:
    print('error')
