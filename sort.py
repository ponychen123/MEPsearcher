#!/usr/bin/python3
#this script sort the PES.data for sake of requirement of xalglib
#ponychen
#20191030

with open("PES.data","r+") as filein:
    data1 = filein.readlines()

data2 = []
for i in data1:
    data2.append(list(map(float, i.split())))

while [] in data2:
    data2.remove([])
data3 = {}
data3[data2[0][1]]=[]

for j in data2:
    if j[1] in data3:
        data3[j[1]].append(j)
    else:
        data3[j[1]]=[]
        data3[j[1]].append(j)

data3 = sorted(data3.items(),key=lambda x:x[0])

tmp = [] 
for k in data3:
    tmp.append(k[1])

for m in tmp:
    m = sorted(m,key=lambda x:x[0])

data4 = tmp

with open("PES.data","w+") as fileout:
    for i in data4:
        for j in i:
            fileout.write("%9.6f  %9.6f  %9.6f\n" %(j[0],j[1],j[2]))


