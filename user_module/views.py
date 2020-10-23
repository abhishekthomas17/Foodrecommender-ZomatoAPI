from django.shortcuts import render,redirect
from . forms import UserRegisterForm
from django.contrib import messages
# Create your views here.
from food_module.models import dish,ingredient,step,nutrition
import pickle
from django.contrib.auth.decorators import login_required
def home(request):
    # with open("data.pickle","rb") as f:
    #     dic1=pickle.load(f)
    #     print(dic1)
    # for i in dic1:
    #     d = dish(name=dic1[i]["name"],minutes=dic1[i]["minutes"],description=dic1[i]["description"])
    #     d.save()
    #
    #     for j in dic1[i]["ingredients"]:
    #         ing = ingredient(name=j,dish=d)
    #         ing.save()
    #
    #     step_count=1
    #     for k in dic1[i]["steps"]:
    #         step_temp = step(description=k,dish=d,number=step_count)
    #         step_count+=1
    #         step_temp.save()
    #
    #     j = dic1[i]["nutrition"]
    #     nut = nutrition(calories=j["calories"],total_fat=j["total fat"],carbohydrates=j["carbohydrates"],sugar=j["sugar"],
    #     sodium=j["sodium"],protein=j["protein"],saturated_fat=j["saturated fat"],dish=d)
    #     nut.save()

    return render(request,"home.html")

def register(request):
    if request.method=="POST":
        forms = UserRegisterForm(request.POST)
        if forms.is_valid():
            forms.save()
            print("Saved")
            username=forms.cleaned_data.get('username')
            # messages.success(request,f'Account Created For {username}')
            return redirect('login')

    else:
        forms = UserRegisterForm()

    return render(request,"register.html",{"form":forms})
