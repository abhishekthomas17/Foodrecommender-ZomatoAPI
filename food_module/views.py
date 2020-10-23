from django.shortcuts import render,redirect
from django.db.models import Q
# Create your views here.
from .models import ingredient,dish,step,nutrition
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import json
import pickle
import operator
import random
import requests
from django.http import HttpResponse,JsonResponse
from pprint import pprint


def view_restaurent(request,pk,city,pk1):
    url = "https://developers.zomato.com/api/v2.1/restaurant?res_id="+str(pk1)
    print(pk1)
    header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": "ae3d26bbe914a5681234df4a9486f038"}
    response = requests.get(url, headers=header)
    response=response.json()
    restaurant={}
    restaurant["name"]=response['name']
    restaurant["url"]=response['url']
    location=[]
    for j in response['location']:
        location.append(response['location'][j])
    restaurant['location']=location
    restaurant["cuisines"]=response['cuisines']
    restaurant["timings"]=response['timings']
    restaurant["photos_url"]=response['photos_url']
    restaurant["events_url"]=response['events_url']
    restaurant["menu_url"]=response['menu_url']
    restaurant["url"]=response['url']
    restaurant["phone_numbers"]=response['phone_numbers']
    restaurant["average_rating"]=response['user_rating']['aggregate_rating']
    restaurant["votes_number"]=response['user_rating']['votes']
    restaurant["rating_color"]=response['user_rating']['rating_color']
    restaurant["cost"]=response['currency'] + str(response['average_cost_for_two'])
    return render(request,'view_restaurent.html',{"restaurant":restaurant,"city":city,"pk":pk,"pk1":pk1})
    return JsonResponse(response)


def ajax_get_restaurents(request):
    cuisines_list= request.GET.getlist('cuisines[]')
    url = "https://developers.zomato.com/api/v2.1/search?entity_id="+str(request.GET.get("pk"))+"&entity_type=city"
    header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": "ae3d26bbe914a5681234df4a9486f038"}
    response = requests.get(url, headers=header)
    response=response.json()
    restaurants=[]
    for i in response['restaurants']:
        restaurant={}
        name=i['restaurant']['name']
        url =i['restaurant']['url']
        location=[]
        for j in i['restaurant']['location']:
            location.append(i['restaurant']['location'][j])
        timings= i['restaurant']['timings']
        cuisines= i['restaurant']['cuisines']

        cost=i['restaurant']['currency'] + str(i['restaurant']['average_cost_for_two'])
        restaurant["id"]=i['restaurant']['id']
        restaurant["name"]=name
        restaurant["url"]=url
        restaurant["location"]=location
        restaurant["timings"]=timings
        restaurant["cuisines"]=cuisines
        restaurant["cost"]=cost
        for k in cuisines_list:
            if k in cuisines:
                restaurants.append(restaurant)
                break
    return render(request,'ajax/ajax_restaurents.html',{"restaurants":restaurants,"city":request.GET.get("city"),"pk":int(request.GET.get("pk"))})

def get_restaurents(request,pk,city):
    url1 = "https://developers.zomato.com/api/v2.1/cuisines?city_id="+str(pk)
    header1 = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": "ae3d26bbe914a5681234df4a9486f038"}
    response1 = requests.get(url1, headers=header1)
    response1=response1.json()
    list_cuisines=[]
    for i in response1['cuisines']:
        list_cuisines.append((i['cuisine']['cuisine_name']))

    url = "https://developers.zomato.com/api/v2.1/search?entity_id="+str(pk)+"&entity_type=city"
    header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": "ae3d26bbe914a5681234df4a9486f038"}
    response = requests.get(url, headers=header)
    response=response.json()
    restaurants=[]
    for i in response['restaurants']:
        restaurant={}
        name=i['restaurant']['name']
        url =i['restaurant']['url']
        location=[]
        for j in i['restaurant']['location']:
            location.append(i['restaurant']['location'][j])
        timings= i['restaurant']['timings']
        cuisines= i['restaurant']['cuisines']

        cost=i['restaurant']['currency'] + str(i['restaurant']['average_cost_for_two'])
        restaurant["id"]=i['restaurant']['id']
        restaurant["name"]=name
        restaurant["url"]=url
        restaurant["location"]=location
        restaurant["timings"]=timings
        restaurant["cuisines"]=cuisines
        restaurant["cost"]=cost
        restaurants.append(restaurant)

    # return JsonResponse(response)
    return render(request,'get_restaurents.html',{"list_cuisines":list_cuisines,"restaurants":restaurants,"city":city,"pk":pk})

@login_required
def zomato_search(request):
    return render(request,'zomato_search.html')

def ajax_zomato_cities(request):
    url = "https://developers.zomato.com/api/v2.1/cities?q="+request.GET.get('search')
    header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": "ae3d26bbe914a5681234df4a9486f038"}
    response = requests.get(url, headers=header)
    return render(request,'ajax/zomato_cities.html',{"cities":response.json()['location_suggestions']})
    return HttpResponse(response.json()['location_suggestions'])

@login_required
def recommender_select(request):
    dishes=dish.objects.all()
    try:
        selected_dishes=request.session['selected_dishes']
    except:
        request.session['selected_dishes'] = []
        selected_dishes=[]
    return render(request,"recommender_select.html",{"selected_dishes":selected_dishes,"dishes":dishes})

def recommender(request):
    selected_dishes=request.session['selected_dishes']
    if len(selected_dishes)<3:
        messages.error(request, 'Please select atleast 3 Dishes')
        return redirect('recommender_select')

    with open("sim_matrix.pickle","rb") as file:
        item_rating=pickle.load(file)

    l=selected_dishes[:]

    score={}
    for d1 in item_rating:
        if d1 in l:
            continue
        sim=0
        total=0

        for d in l:
            sim = sim+item_rating[d1][d]
            # total = total+(item_rating[d1][d]*l[d])
        score[d1] = sim
    l1=list(reversed(sorted(score.items(), key=operator.itemgetter(1))))
    l1=[i[0] for i in l1]
    a=[]
    for i in l1:
        a.append(dish.objects.get(name=i))
    return render(request,"recommender.html",{"r":item_rating,"l":a[:5],"selected":selected_dishes})

def view_dish(request,pk):
    dish_obj = dish.objects.get(pk=pk)
    ingredients = ingredient.objects.filter(dish=dish_obj)
    steps = step.objects.filter(dish=dish_obj)
    nutritions = nutrition.objects.get(dish=dish_obj)

    fin_steps = [0]*len(steps)
    for i in steps:
        fin_steps[i.number-1]=i
    return render(request,"view_dish.html",{"dish":dish_obj,"ingredients":ingredients,"steps":fin_steps,"nutritions":nutritions})

def view_dish1(request,pk):
    dish_obj = dish.objects.get(pk=pk)
    ingredients = ingredient.objects.filter(dish=dish_obj)
    steps = step.objects.filter(dish=dish_obj)
    nutritions = nutrition.objects.get(dish=dish_obj)

    fin_steps = [0]*len(steps)
    for i in steps:
        fin_steps[i.number-1]=i
    return render(request,"view_dish1.html",{"dish":dish_obj,"ingredients":ingredients,"steps":fin_steps,"nutritions":nutritions})

@login_required
def search_food(request):
    try:
        selected_ingredients=request.session['selected_ingredients']
    except:
        request.session['selected_ingredients'] = []
        selected_ingredients=[]
    if 'add_ingredient' in request.GET:
        print(request.GET.get('add_ingredient'))

    return render(request,"search_food.html",{"selected_ingredients":selected_ingredients})


def find_dishes(request):
    selected_ingredients=request.session['selected_ingredients']
    if len(selected_ingredients)<3:
        messages.error(request, 'Please select atleast 3 ingredients')
        return redirect('search_food')
    # total_ingredients=[]
    # for i in selected_ingredients:
    #     ingredients=ingredient.objects.filter(
    #     Q(name__icontains=i)
    #     ).distinct()
    #     for j in ingredients:
    #         total_ingredients.append(j)
    selected_ingredients = [i.lower() for i in selected_ingredients]

    dishes = dish.objects.all()
    all_dishes=[]
    for i in dishes:
        cnt=0
        cnt1=0
        ing = ingredient.objects.filter(dish=i)
        for j in ing:
            if j.name.lower() in selected_ingredients:
                cnt+=1
        print(cnt/len(ing))
        if cnt/len(ing) > 0.1:
            all_dishes.append(i)
    return render(request,"find_dishes.html",{"selected_ingredients":selected_ingredients,"all_dishes":all_dishes})


def search_ingredients(request):
    query = request.GET.get("search")
    ingredients=ingredient.objects.filter(
    Q(name__icontains=query)
    ).distinct()
    ingredients1=[]
    for i in ingredients:
        if i.name not in ingredients1:
            ingredients1.append(i.name)
    return render(request,"ajax/search_ingredients.html",{"ingredients":ingredients1})


def add_ingredient(request):
    val = request.GET.get("val")
    selected_ingredients=request.session['selected_ingredients']
    if val not in selected_ingredients:
        selected_ingredients.append(val)
    request.session['selected_ingredients'] = selected_ingredients
    return render(request,"ajax/add_ingredient.html",{"selected_ingredients":selected_ingredients})

def delete_ingredient(request):
    val = request.GET.get("val")
    selected_ingredients=request.session['selected_ingredients']
    selected_ingredients.pop(selected_ingredients.index(val))
    request.session['selected_ingredients'] = selected_ingredients
    return render(request,"ajax/delete_ingredient.html",{"selected_ingredients":selected_ingredients})


def add_dish(request):
    dishes=dish.objects.all()
    val = request.GET.get("val")
    selected_dishes=request.session['selected_dishes']
    if val not in selected_dishes:
        selected_dishes.append(val)
    request.session['selected_dishes'] = selected_dishes
    return render(request,"ajax/add_dish.html",{"selected_dishes":selected_dishes,"dishes":dishes})



def delete_dish(request):
    dishes=dish.objects.all()
    val = request.GET.get("val")
    selected_dishes=request.session['selected_dishes']
    selected_dishes.pop(selected_dishes.index(val))
    request.session['selected_dishes'] = selected_dishes
    return render(request,"ajax/delete_dish.html",{"selected_dishes":selected_dishes,"dishes":dishes})
