import pandas as pd
import csv
import pickle

dic={}

all_ingredients=[]
all_tags=[]
min_nut=[1000]*7
max_nut=[-1000]*7
with open('RAW_recipes.csv', 'r',encoding="utf8") as file:
    reader = csv.reader(file)
    i=0
    for row in reader:
        if i==0:
            i+=1
            continue

        res1 = row[10].strip('][').split(', ')
        for k in res1:
            k=k.strip("'")
            if k not in all_ingredients:
                all_ingredients.append(k)
        
        res_tags = row[5].strip('][').split(', ')
        for k in res_tags:
            k=k.strip("'")
            if k not in all_tags:
                all_tags.append(k)

        res2 = row[6].strip('][').split(', ')
        for k in range(0,len(res2)):
            min_nut[k]=min(min_nut[k],float(res2[k]))
            max_nut[k]=max(max_nut[k],float(res2[k]))
        i+=1
        if i==500:
            break

print(min_nut,max_nut)

with open("ingredients.pickle","wb") as f:
    pickle.dump(all_ingredients,f)

with open("tags.pickle","wb") as f:
    pickle.dump(all_tags,f)

with open("min_nut.pickle","wb") as f:
    pickle.dump(min_nut,f)


with open("max_nut.pickle","wb") as f:
    pickle.dump(max_nut,f)
    
##with open("data.pickle","rb") as f:
##    dic1=pickle.load(f)
##    print(dic1)
