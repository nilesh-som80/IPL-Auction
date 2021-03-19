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
    path("playersdetail", views.index, name="index"),
    path("pay/<int:player_id>",views.pay,name="pay"),
    path("profile/<int:player_id>", views.profile, name="profile"),
    path("IPLSTATS/<int:player_id>", views.ipl, name="ipl"),
    path("ODISTATS/<int:player_id>", views.odi, name="odi"),
    path("TESTSTATS/<int:player_id>", views.test, name="test"),
    path("T20ISTATS/<int:player_id>", views.t20i, name="t20i"),
    path("Delete/<int:player_id>", views.delete, name="delete"),
    path("userlist", views.userlist, name="userlist"),
    path("userdetail/<str:uid>",views.userdetail, name="userdetail"),
    path("deleteuser/<str:uid>", views.deleteuser, name="deleteuser"),
    path("resetplayer", views.resetplayer, name="resetplayer"),
    path("resetuser", views.resetuser, name="resetuser"),
    path("resetpp/<int:player_id>", views.resetpp, name="resetpp"),
]
