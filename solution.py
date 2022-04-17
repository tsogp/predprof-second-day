x = [9, 33, 9, 32]
y = [9, 9, 23, 22]
F = {'5b6eb38b': [0.1626, 0.2667, 0.262, 0.9231], 'c00b92ba': [0.249, 0.6186, 0.1846, 0.4138], '931ede7b': [1.4634, 0.1412, 0.1592], '661c2e66': [0.1859, 0.2262, 0.2703, 0.4587], 'c2958c11': [0.2006, 1.1475, 0.1022, 0.2006], '08d55d4f': [0.2602, 0.1918, 0.6931, 0.4142]}

def rasst(x, y):
    return((x**2 + y**2))

def find_detectors(F, exists, x, y): 
    n=0
    ot=[]
    for detector in F.keys():
        n+=1
        delta=1.024
        numsx=[]
        numsy=[]
        while (len(numsx)==0 or len(numsx)>2):
            numsx=[]
            numsy=[]
            numsk=[]
            koef=0
            delta*=0.8
            for x0 in range(1, 36):
                for y0 in range(1, 36):
                    flag=True
                    for f1 in range(len(F[detector])):
                        for f2 in range(f1+1, len(F[detector])):
                            if exists[detector][f1] and exists[detector][f2]:
                                r1=F[detector][f1]*rasst(x0-x[f1], y0-y[f1])
                                r2=F[detector][f2]*rasst(x0-x[f2], y0-y[f2])
                                if (abs(r2-r1)>delta):
                                    flag=False
                                    koef=r1
                    if flag:
                        numsx.append(x0)
                        numsy.append(y0)
                        numsk.append(koef)
        ot.append([numsx[0], numsy[0], round(numsk[0], 3)])
    return(ot)
        


x = [9, 33, 9, 32]
y = [9, 9, 23, 22]
exists = {'5b6eb38b': [True, True, True, True], 'c00b92ba': [True, True, True, True], '931ede7b': [True, True, True, False], '661c2e66': [True, True, True, True], 'c2958c11': [True, True, True, True], '08d55d4f': [True, True, True, True]}
F = {'5b6eb38b': [0.1626, 0.2667, 0.262, 0.9231], 'c00b92ba': [0.249, 0.6186, 0.1846, 0.4138], '931ede7b': [1.4634, 0.1412, 0.1592, 0.0], '661c2e66': [0.1859, 0.2262, 0.2703, 0.4587], 'c2958c11': [0.2006, 1.1475, 0.1022, 0.2006], '08d55d4f': [0.2602, 0.1918, 0.6931, 0.4142]}

print(find_detectors(F, exists,  x, y))

x1 = [1, 3, 1]
y1 = [1, 3, 3]
exists1 = {"a": [True, True, True]}
F1 = {"a": [1.0, 1.0, 1.0]}
print(find_detectors(F1, exists1,  x1, y1))

def make_matrice():
    pass
                        

