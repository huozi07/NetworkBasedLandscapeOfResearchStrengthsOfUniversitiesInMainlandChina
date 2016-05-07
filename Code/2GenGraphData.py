# coding: utf-8
#将相似矩阵转换为 列表[sourceid,targetid,weight]
import csv
graphdata=file('teacher_def_jiaobing_phase3.csv', 'rb') #打开学校文件
simdata=csv.reader(graphdata)
a=[i for i in simdata]

simlist=[]
for i in range(0,116):
    for j in range(i,116):
        if i!=j: simlist.append(a[i][j])
print len(simlist)


list=[]
for i in range(1,117):
    for j in range(i,117):
        if i!=j:list.append([i,j])
print len(list)

for i in range(0,6670):
   list[i].append(simlist[i])
print len(list)

outfile = file('phase3_graph116.csv', 'wb')#output_filename define
writer = csv.writer(outfile)
for i in range(0,6670): #school number
   writer.writerow(list[i])
outfile.close()