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
from django.urls import path
from . import views

urlpatterns = [
    path('DataEntry',views.dataentry,name='DataEntry'),
    path('DataEntryIPL',views.iplentry,name='DataEntryIPL'),
    path('DataEntryTEST',views.testentry,name='DataEntryTest'),
    path('DataEntryODI',views.odientry,name='DataEntryODI'),
    path('DataEntryT20I',views.t20ientry,name='DataEntryT20I'),
]
