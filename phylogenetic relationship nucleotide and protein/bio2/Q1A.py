import csv
source = open("Nucleotide_alignment.txt")
#print(source)
# def makelists(lst): 
#     res = []
#     for el in lst: 
#         sub = el.split(', ') 
#         res.append(sub)
#     return res

# def file_lengthy(fname):
#         with open(fname) as f:
#                 for i, l in enumerate(f):
#                         pass
#         return i + 1
matrix = []
matrix3 = []
def removearrlines(n,matrix,var1):
    var = ""
    itr = 0
   # print(n)
    for i in range(n):
        if var1[i][0] == '>':
           if itr != 0:
               matrix.append(var)
               itr += 1
               var = ""
           else:
               itr += 1
        else:
            var += var1[i]
       # print(var)
    matrix.append(var)
 #   print(matrix)
    return matrix          
def removenewlines(nucli,n):
    t1 = []
    for i in range(n):
        var = []
        lent = len(nucli[i])
        for j in range(lent):
            if nucli[i][j] == '\n':
                continue
            else:
                var.append(nucli[i][j])
        t1.append(var)
    return t1

def countmismatch(temp,n,nucli):
    matrix2 = []
    for x in range(n):
        var = []
        for y in range(n):
            missmatch = 0
            k = len(temp[x])
            for z in range(k):
                if temp[x][z] == temp[y][z]:
                    continue
                else:
                    missmatch += 1
            val = (missmatch/len(nucli[y]))
            var.append(val)
        matrix2.append(var)
      #  print(matrix2)
    return matrix2
                    
cntarr = 0
# for i in source:
#     c = source.read(1)
# #    #print(c)
#     if c == '>':
# 	    cntarr += 1
#print(cntarr)
var = source
tot_lines = 0
var1 = []
x = ""
for x in var: 
    var1.append(x)
    tot_lines += 1

#print(tot_lines)
#tot_lines = file_lengthy("Nucleotide1.txt")
#tot_lines = file_lengthy("Nucleotide1.txt")
tot = 0
nucli = ""
#print(var1)
nucli = removearrlines(tot_lines,matrix,var1) #removing the lines starting from '>' from the initial list
#print(nucli)
s = len(nucli)
#print(len(nucli[4]))
temp = removenewlines(nucli,s) #removing all the \n from the list nucli and making the required list for the calulation
s = len(temp)
#print(temp)
missmatches = countmismatch(temp,s,nucli) #finding the distance matrix
matrix3 = missmatches
n = len(matrix3)
for i in range(n):
    print(matrix3[i])
ans = open("Ndistance.csv", "w")
writer = csv.writer(ans)
for i in range(len(matrix3)):
    writer.writerow(matrix3[i])
#distance matrix in the Ndistance.csv file is in the same order as it is appeared in Nucleotide_alignment.txt