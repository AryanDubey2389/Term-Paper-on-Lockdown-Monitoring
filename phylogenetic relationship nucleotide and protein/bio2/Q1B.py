import csv
f1 = csv.reader(open("Ndistance.csv","r"), delimiter=',')
s1 = '('
s2 = ')'
s3 = ','
s4 = ':'
d1 = {}
matrix1 = []
matrix2 = []
matrix3 = []
matrix4 = []
matrix5 = []
matrix6 = []
matrix7 = []
l1 = list(f1)
n1 = len(l1)


def chng(l1,n,ds,itr1,itr2):
    var1 = []
    var2 = []
    for x in range(n):
        if x == itr2:
            continue
        elif x != itr1 and x != itr2:
            var1.append((float(ds[itr1][x])+float(ds[itr2][x]))/2)
            var2.append((float(ds[x][itr1])+float(ds[x][itr2]))/2)
            continue
        else:
            var1.append(0)
            var2.append(0)
            
    l1.pop(itr2)
    for x in range(len(l1)):
        l1[x][itr1] = var2[x]
    return var1
def boolean1(d,k):
    if k in d:
        return 1
    else:
        return 0
    
def boolean(d, k,mn):
    if k in d:
        return str(float(float(mn)/2) - float(d[k]))
    return str(float(float(mn)/2))

def ans(n):
    itr1 = 0
    itr2 = 0
    mn = 1e18
    var = n
    key = [' ','A', 'B', 'C','D','E','F','G','H','I','J']
    ds = l1
    while True:
        mim = float(mn)
        if var - 1:
            # print(key)
            # for x in range(var):
            #     s1 = str(key[x + 1]) + " "
            #     s2 = str(l1[x])
            #     print(s1 + s2)
            for x in range(var):
                k = len(l1[x])
                for y in range(k):
                    if float(l1[x][y])!=0:
                        if float(l1[x][y]) < float(mim):
                            mim = l1[x][y]
                            itr1 = x
                            itr2 = y
                #print(l1[itr2])
            # print("itr1,itr2",itr1+1,itr2+1)
            # print(key[itr2+1])
            s5 = key[itr1 + 1]
            s6 = key[itr2 + 1]
            ans1 = boolean(d1,key[itr1+1],mim)
            ans2 = boolean(d1,key[itr2+1],mim)
            key[itr1+1]= s1 + s5 + s4 + ans1 + s3 + s6 + s4 +ans2+ s2
            d1[key[itr1+1]]=float(mim)/2
            if boolean1(d1,key[itr2+1]):
                d1.pop(key[itr2+1])
            n2 = len(l1)
            var1 = chng(l1, n2, ds, itr1, itr2)
            [j.pop(itr2) for j in l1]
            if itr1 < itr2:
                l1[itr1] = var1
            else:
                l1[itr1-1] = var1
           # for i in range(len(l1)):
            #    print(l1[i])
                #print(len(l1))
            ds = []
            for x in range(len(l1)):
                ds.append(l1[x])
            var = len(l1)
            key.pop(itr2+1)
        else:
            break
    return key[1]

def grd(n):
    var1 = []
    var2 = []
    for x in range(n):
        var3 = []
        s5 = str(x+1) 
        for y in range(n):
            s6 = str(y+1)
            var3.append(s1 + s5 + s3 + s6 + s2)
        var1.append(var3)
    return var1

matrix1 = grd(n1) #grid
fin = ans(n1) # storing the final result
print(fin)
Poutput = open("q1b.txt", "w")
Poutput.write(fin)
writer = csv.writer(Poutput)
# A, B, C, D , E, F, G , H, I are in the same order as it in the Nucleotide_alignment.txt file
# That is the first is A, second is B and so on.

