"""esummit21 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from . import views

urlpatterns = [
     path('login', views.login,name="login"),
     path('logout', views.logout,name="logout"),
     path('signup', views.signup,name="signup"),
     path('player/<int:player_id>', views.profile,name="profile"),
     path('main', views.main_page,name="main"),
     path('batsman',views.batsman,name="batsman"),
     path('bowler',views.bowler,name="bowler"),
     path('keeper',views.keeper,name="keeper"),
     path('allrounder',views.allrounder,name="allrounder"),
     path('users_dashboard',views.users_dashboard,name="users_dashboard"),
     path('load/<int:player_id>', views.bid_load_data, name="bid_load_data")

]
