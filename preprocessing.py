import pandas as pd
import csv
import pickle

dic={}

with open('RAW_recipes.csv', 'r',encoding="utf8") as file:
    reader = csv.reader(file)
    i=0
    for row in reader:
        if i==0:
            i+=1
            continue
        temp={}

        temp["name"] = row[0]
        temp["minutes"]=int(row[2])
        
        res = row[8].strip('][').split(', ')
        steps=[]
        for k in res:
            k=k.strip("'")
            steps.append(k)
        temp["steps"]=steps

        if row[9].strip()=="":
            continue
        temp["description"]=row[9].strip().replace("\n"," ")

        res1 = row[10].strip('][').split(', ')
        ingredients=[]
        for k in res1:
            k=k.strip("'")
            ingredients.append(k)

      
        temp["ingredients"]=ingredients

        res2 = row[6].strip('][').split(', ')
        nut={}
        nut["calories"]=float(res2[0])
        nut["total fat"]=float(res2[1])
        nut["sugar"]=float(res2[2])
        nut["sodium"]=float(res2[3])
        nut["protein"]=float(res2[4])
        nut["saturated fat"]=float(res2[5])
        nut["carbohydrates"]=float(res2[6])
        temp["nutrition"]=nut

        tags=[]
        res_tags = row[5].strip('][').split(', ')
        for k in res_tags:
            k=k.strip("'")
            tags.append(k)
        
        temp["tags"]=tags
        
        dic[i]=temp
        i+=1
        if i==500:
            break

print(dic)

with open("data_sim.pickle","wb") as f:
    pickle.dump(dic,f)

##with open("data.pickle","wb") as f:
##    pickle.dump(dic,f)
####    dic1=pickle.load(f)
####    print(dic1)
