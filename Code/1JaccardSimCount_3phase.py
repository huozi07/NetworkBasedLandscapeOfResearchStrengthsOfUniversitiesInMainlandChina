#coding: utf-8
#Compute the correlation coefficient matrix between universities in different stages.
import csv

sumcatecount= file('cate_count_phase1.csv', 'rb') #ReadFile
schoolread=csv.reader(sumcatecount)


def Jaccard_Sim_Compute(school1,school2):
    sum_sim=0
    b=0
    for k in range(1,102):
        school1[k]=float(school1[k])
        school2[k]=float(school2[k])
        if max(school1[k],school2[k])==float(0):
            a=0
            b+=1
        else:
            a=float(min(school1[k],school2[k])/max(school1[k],school2[k]))
        sum_sim+=a

    if b==101:
          sim=0
    else:
          sim=sum_sim/(101-b)
    return sim

if __name__=="__main__":
  a=[i for i in schoolread]
  print "number of school item"
  print len(a[2])
  print "total school num"
  print len(a)
  list=[]
  for i in range(1,117):      
    s=[]  #cache list
    for j in range(1,117):
        sim=Jaccard_Sim_Compute(a[i],a[j]) 
        s.append(sim)
    list.append(s)

  outfile = file('SimMatrixResult_phase1.csv', 'wb')    #output_filename
  writer = csv.writer(outfile)
  for i in range(0,116): #school number
     writer.writerow(list[i])
  outfile.close()
  
  
  
  
  
  