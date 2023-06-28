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

from .models import *
from .restapis import get_request, get_dealers_from_cf, get_dealer_by_id_from_cf, get_dealer_reviews_from_cf, post_request, analyze_review_sentiments




# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.
def home(request):

    return render(request, 'home.html', {})

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
    if request.method == "GET":
        context = {}
        url = "https://us-south.functions.appdomain.cloud/api/v1/web/f8c68992-0352-4114-b193-40963503b670/dealership-package/get-dealership"
        print("=====", url)
        dealerships = get_dealers_from_cf(url)
        context["dealership_list"] = dealerships

        return render(request, 'djangoapp/index.html', context)



def get_dealer_details(request, dealer_id):
    context = {}
    if request.method == "GET":
        url = "https://us-south.functions.appdomain.cloud/api/v1/web/f8c68992-0352-4114-b193-40963503b670/dealership-review-package/get-dealership-reviews?id={0}".format(dealer_id)
        reviews = get_dealer_reviews_from_cf(url, dealer_id=dealer_id)

        return render(request, 'djangoapp/dealer_details.html', {"reviews":  reviews, "dealer_id": dealer_id})


# Create a `get_dealer_details` view to render the reviews of a dealer
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request, dealer_id):
# ...

# View to submit a new review
def add_review(request, id):
    context = {}
    dealer_url = "https://us-south.functions.appdomain.cloud/api/v1/web/f8c68992-0352-4114-b193-40963503b670/dealership-package/get-dealership"
    # dealer = get_dealer_by_id_from_cf(dealer_url, dealer_id=id)
    context["id"] = id
    if request.method == 'GET':
        # Get cars for the dealer
        cars = CarModel.objects.all()
        print(cars)
        context["cars"] = cars
        
        return render(request, 'djangoapp/add_review.html', context)
    elif request.method == 'POST':
        if request.user.is_authenticated:
            username = request.user.username
            print(request.POST)
            payload = dict()
            car_id = request.POST["car"]
            car = CarModel.objects.get(pk=car_id)
            payload["time"] = datetime.utcnow().isoformat()
            payload["name"] = username
            payload["dealership"] = id
            payload["id"] = id
            payload["review"] = request.POST["content"]
            payload["purchase"] = False
            if "purchasecheck" in request.POST:
                if request.POST["purchasecheck"] == 'on':
                    payload["purchase"] = True
            payload["purchase_date"] = request.POST["purchasedate"]           
            payload["car_model"] = car.name
            new_payload = {}
            new_payload["review"] = payload
            review_post_url = "https://us-south.functions.appdomain.cloud/api/v1/web/f8c68992-0352-4114-b193-40963503b670/post-reviews-package/post-reviews"

            post_request(review_post_url, new_payload, id=id)
        return redirect("/dealer-details/%s/"%id)

