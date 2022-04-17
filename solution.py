x = [9, 33, 9, 32]
y = [9, 9, 23, 22]
F = [[0.1626, 0.2667, 0.262, 0.9231]]

def rasst(x, y):
    return((x**2 + y**2))

for detector in range(1):
    delta=0.1
    numsx=[]
    numsy=[]
    while (len(numsx)!=1):
        numsx=[]
        numsy=[]
        delta*=0.8
        for x0 in range(1, 36):
            for y0 in range(1, 36):
                flag=True
                for f1 in range(4):
                    for f2 in range(f1+1, 4):
                        r1=F[detector][f1]*rasst(x0-x[f1], y0-y[f1])
                        r2=F[detector][f2]*rasst(x0-x[f2], y0-y[f2])
                        if (abs(r2-r1)<=delta):
                            numsx.append(x0)
                            numsy.append(y0)
    print(detector, ":", *numsx, *numsy)

                        

