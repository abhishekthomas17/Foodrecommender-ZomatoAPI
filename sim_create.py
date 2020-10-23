import pandas as pd
import csv
import pickle
import math



with open("min_nut.pickle","rb") as f:
    min_nut=pickle.load(f)
    print(min_nut)

with open("max_nut.pickle","rb") as f:
    max_nut=pickle.load(f)
    print(max_nut)


with open("sim_temp.pickle","rb") as f:
    sim_temp=pickle.load(f)


sim={}
for i in sim_temp:
    sim1={}
    for j in sim_temp:
        if str(i)==str(j):
            continue

        a=sim_temp[i]["ingredients"]+sim_temp[i]["tags"]
        b=sim_temp[j]["ingredients"]+sim_temp[j]["tags"]
        num=0
        den1=0
        den2=0
        den=0
        for p in range(0,len(a)):
            num=num+a[p]*b[p]
            den1=den1+a[p]*a[p]
            den2=den2+b[p]*b[p]
        for k in range(0,len(sim_temp[i]["nutrition"])):
            num=num+(1-abs(sim_temp[i]["nutrition"][k]-sim_temp[j]["nutrition"][k]))/max_nut[k]
            den1=den1+(abs(sim_temp[i]["nutrition"][k])/max_nut[k])**2
            den2=den2+(abs(sim_temp[j]["nutrition"][k])/max_nut[k])**2
        den=(math.sqrt(den1))*(math.sqrt(den2))    
        if den==0:
            sim1[j]=0
        else:
            sim1[j]=num/den
    sim[i]=sim1

for i in sim:
    print(sim[i])
    break


with open("sim_matrix.pickle",'wb') as dic:
     pickle.dump(sim,dic,protocol=pickle.HIGHEST_PROTOCOL)
