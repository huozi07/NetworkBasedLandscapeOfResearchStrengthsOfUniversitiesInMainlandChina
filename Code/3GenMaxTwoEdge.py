import csv
import re
def LoadData():
    #networkData=csv.reader(file('phase1nodeAttributeFromNetdraw.txt', 'rb'))
    txtpath=r"phase1nodeAttributeFromNetdraw.txt"
    fp=open(txtpath)
    arr=[]
    for lines in fp.readlines():
       lines=lines.replace("\n","").split(",")
       arr.append(lines)
    fp.close()
    community=[]
    for i in arr[2:118]:
        community.append(i[1][1])
    node=[]
    for i in arr[120:236]:
        fenci=re.compile(r' ').split(i[0])
        node.append(fenci[0])
    data=[]
    for i in range(116):
        data.append([node[i],community[i]])
    print data[0:4]
    return data

def outEdge(networkEdge):
    outfile = file('phase1_all_max_two_node_community.csv', 'wb')    #output_filename define
    writer = csv.writer(outfile)
    writer.writerow(['node','community'])
    for i in range(0,len(networkEdge)):
         writer.writerow(networkEdge[i])

if __name__=="__main__":
    networkEdge=LoadData()
    #outEdge(networkEdge)


