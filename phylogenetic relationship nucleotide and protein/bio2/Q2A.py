import csv
source = open("Protein_alignment.txt")
matrix1 = []
matrix1 = []
matrix2 = []
matrix3 = []
matrix4 = []
matrix5 = []
matrix6 = []
matrix7 = []

def cntlines(source):
    cnt = 0
    for i in source:
        matrix1.append(i)
        cnt += 1
    return cnt

def getting_lines(f2):
    temp = []
    for i in f2:
        temp.append(i)
    return temp

def removearrlines(n):
    var = ""
    itr = 0
    temp = []
    for i in range(n):
        if matrix1[i][0]=='>' and itr == 0:
            itr = itr + 1
        elif matrix1[i][0]=='>' and itr > 0:
            temp.append(var)
            var=""
        else:
            var = var + matrix1[i]
    temp.append(var)
    return temp    

def removenewlines(nucli,n):
    temp = []
    for i in range(n):
        var = []
        lent = len(nucli[i])
        for j in range(lent):
            if nucli[i][j] == '\n':
                continue
            else:
                var.append(nucli[i][j])
        temp.append(var)
    return temp

def mat(n,lines):
    temp = []
    temp1 = []
    for i in range(n):
        if lines[i][0] != '*':
            temp = lines[i].split()
            t = len(temp) - 1
            temp = temp[1:t]
            temp1.append(temp)
    return temp1

def countscore(temp1,score,cnt):
    temp3 = []
    if len(temp1) == 1:
        score -= 11
    elif len(temp1) > 1:
        for m in range(len(temp1)):
            if m != 0:
                temp3.append(temp1[m] - temp1[m-1])
        for m in range(len(temp1)):
            if m==0:
               cnt = 1
               continue
            if temp3[m-1] == 1:
               cnt += 1
            elif temp3[m-1]!=1:
               score -= (10 + cnt)
               cnt = 1
        score -= (10 + cnt)
    return [score,cnt]
def f1(nstr,n): # need to be changed
    #print(nstr)
    #print(n)
    for x in range(n):
        temp = []
        for y in range(n):
            temp1 = []
            temp2 = []
            score  = 0
            k = len(nstr[y])
            for z in range(k):
                if nstr[x][z] != '-':
                    if nstr[y][z] != '-':
                        score += int(matrix2[keys[nstr[x][z]]][keys[nstr[y][z]]])
                    if nstr[y][z] == '-':
                        temp2.append(z)
                else:
                    if nstr[y][z] != '-':
                        temp1.append(z)
            temp1.sort()
            temp2.sort()
            # print(temp1)
            # print(temp2)
            temp3 = []
            temp4 = []
            cnt = 0
            score1 = countscore(temp1,score,cnt)
            score = score1[0]
            cnt = score1[1]
            # print(score)
            # print(cnt)
            score2 = countscore(temp2,score,cnt)
            score = score2[0]

            temp.append(score)
        matrix4.append(temp)   
    return matrix4 
            
            
              
       
no_of_lines_in_source = cntlines(source) 
#print(no_of_lines)
newstring = removearrlines(no_of_lines_in_source) #removing all the lines with '<' and making list of other
l1 = len(newstring)
# print(l1)
# print(newstring)
newstring1 = removenewlines(newstring,l1)
l2 = len(newstring1)
# print(newstring1)
f2 = open("BLOSUM62.txt")
no_of_lines_in_f2 = cntlines(f2)
f2.close()
f2 = open("BLOSUM62.txt")
lines = getting_lines(f2)
#print(no_of_lines_in_f2)
#print(lines)
keys={'A':0,'R':1,'N':2,'D':3,'C':4,'Q':5,'E':6,'G':7,'H':8,'I':9,'L':10,'K':11,'M':12,'F':13,'P':14,'S':15,'T':16,'W':17,'Y':18,'V':19,'B':20,'Z':21,'X':22 }
matrix2 = mat(no_of_lines_in_f2,lines)
#print(matrix2)
ans = f1(newstring1,l2)
for i in range(len(ans)):
    print(ans[i])
Poutput = open("Pdistance.csv", "w")
writer = csv.writer(Poutput)
for i in range(len(ans)):
	writer.writerow(ans[i])
Poutput.close()
#score matrix in the Pdistance.csv file is in the same order as it is appeared in Protein_alignment.txt





