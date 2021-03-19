from django.shortcuts import render,redirect

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('ed-cell-esummit21-firebase-adminsdk-qjav8-eb7c154124.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://ed-cell-esummit21-default-rtdb.firebaseio.com/'
})

def index(request):
    return redirect("/user/login")




