def z3(x):
    xmin=x[0]
    index=0
    ind=[]
    for i in range (1,len(x)):
        if (x[i]<xmin):
            xmin=x[i]
            index=i
    for i in range (len(x)):
        if (x[i]==xmin):
            ind.append(i)
    print('The lowest value in the provided array is', xmin, 'located on the', ind, 'index/indexes')

z3([0, -10, 54, 6])
