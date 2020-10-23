import pandas as pd
import csv
import pickle



with open("data_sim.pickle","rb") as f:
    dic=pickle.load(f)
    print(dic[1])

with open("tags.pickle","rb") as f:
    all_tags=pickle.load(f)
    print(all_tags)

with open("ingredients.pickle","rb") as f:
    all_ingredients=pickle.load(f)
    print(all_ingredients)

 

sim={}
for i in dic:
    temp={}
    ingredients = [0]*len(all_ingredients)
    tags = [0]*len(all_tags)

    for j in dic[i]["ingredients"]:
        try:
            ingredients[all_ingredients.index(j)]=1
        except:
            pass
    

    for k in dic[i]["tags"]:
        try:
            tags[all_tags.index(k)]=1
        except:
            pass
    temp["ingredients"]=ingredients
    temp["tags"]=tags
    temp["minutes"]=dic[i]["minutes"]
    nut=[]
    for k in dic[i]["nutrition"]:
        nut.append(float(dic[i]["nutrition"][k]))
    temp["nutrition"]=nut
    sim[dic[i]["name"]]=temp

with open("sim_temp.pickle","wb") as f:
    pickle.dump(sim,f)
