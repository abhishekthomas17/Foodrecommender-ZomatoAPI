"""food_recommender URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from user_module import views as uviews
from food_module import views as fviews
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",uviews.home,name='home'),
    path("register/",uviews.register,name='register'),
    path("login/",auth_views.LoginView.as_view(template_name="login.html"),name='login'),
    path("logout/",auth_views.LogoutView.as_view(template_name="logout.html"),name='logout'),

    path("search_food/",fviews.search_food,name='search_food'),
    path("find_dishes/",fviews.find_dishes,name='find_dishes'),
    path("view_dish/<int:pk>",fviews.view_dish,name='view_dish'),
    path("view_dish1/<int:pk>",fviews.view_dish1,name='view_dish1'),
    path("ajax/search_ingredients/",fviews.search_ingredients,name='search_ingredients'),
    path("ajax/add_ingredient/",fviews.add_ingredient,name='add_ingredient'),
    path("ajax/delete_ingredient/",fviews.delete_ingredient,name='delete_ingredient'),
path("ajax/add_dish/",fviews.add_dish,name='add_dish'),
path("ajax/delete_dish/",fviews.delete_dish,name='delete_dish'),


    path("recommender/",fviews.recommender,name='recommender'),
    path("recommender_select/",fviews.recommender_select,name='recommender_select'),


        path("ajax/zomato_cities/",fviews.ajax_zomato_cities,name='ajax_zomato_cities'),
        path("zomato_search/",fviews.zomato_search,name='zomato_search'),
        path("get_restaurents/<int:pk>/<str:city>",fviews.get_restaurents,name='get_restaurents'),
        path("ajax/get_restaurents/",fviews.ajax_get_restaurents,name='ajax_get_restaurents'),
        path("get_restaurents/<int:pk>/<str:city>/view_restaurent/<int:pk1>/",fviews.view_restaurent,name='view_restaurent')

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
