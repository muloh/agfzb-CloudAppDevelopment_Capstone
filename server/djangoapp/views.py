from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
# from .models import related models
# from .restapis import related methods
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from datetime import datetime
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.


# Create an `about` view to render a static about page
def about(request):

    return render(request, 'djangoapp/about.html', {})

# Create a `contact` view to return a static contact page
def contact(request):
    return render(request, 'djangoapp/contact.html', {})

# Create a `login_request` view to handle sign in request
def login_request(request):
    user = request.user
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username = username, password = password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/djangoapp/')
        else:
            return render(request, 'djangoapp/login.html', {'user': user})
    else:
        return render(request, 'djangoapp/login.html', {'user':user})


# Create a `logout_request` view to handle sign out request
def logout_request(request):
    logout(request)
    return HttpResponseRedirect('/djangoapp/')



# Create a `registration_request` view to handle sign up request
def registration_request(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']

        if not (password == confirm_password):
            error_msg = "Passwords do not match"
            return render(request, 'djangoapp/registration.html', {'error_msg':error_msg})

        user_exist = False

        try:
            User.objects.get(username = username) # checking if user exist  
            user_exist = True
        except:
            print(' %s is a new user '%username)

        if not user_exist:
            user = User.objects.create_user(username = username, email=email, first_name = first_name, last_name = last_name)
            login(request, user)
            return HttpResponseRedirect('/')
    else:
        return render(request, 'djangoapp/registration.html', {})



# Update the `get_dealerships` view to render the index page with a list of dealerships
def get_dealerships(request):
    context = {}
    if request.method == "GET":
        return render(request, 'djangoapp/index.html', context)


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

