##### Belt Exam - Login App
##### Mason Brewer
##### November 19th, 2018

from django.shortcuts import render, redirect
from time import gmtime, strftime
import random, datetime, bcrypt
from .models import *
from django.contrib import messages

# create a regular expression object that we'll use later   
# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


def addUser(data):
    # Hashing given password.
    password = data["password"]
    passHash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    # Adding user
    newUser = User.objects.create(firstName=data["firstName"], lastName=data["lastName"], email=data["email"], passHash=passHash)
    return newUser

def loginReg(request):
    if not "isLoggedIn" in request.session:
        request.session["isLoggedIn"] = False
    if not "thisUserID" in request.session:
        request.session["thisUserID"] = None
    elif request.session["isLoggedIn"]:
        return redirect("/success")
    return render(request,'loginApp/registration.html')

# POST
def processLogin(request):
    if request.method == "GET":
        return redirect("/login")
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for k in errors:
                messages.error(request, errors[k], extra_tags = k)
            print("failure!")
            return redirect("/login")
        else:
            print("success!")
            request.session["isLoggedIn"] = True
            request.session["thisUserID"] = User.objects.get(email = request.POST["email"]).id
            return redirect("/belt")

# POST
def processReg(request):
    if request.method == "GET":
        return redirect("/login")
    if request.method == "POST":
        errors = User.objects.register_validator(request.POST)
        if len(errors) > 0:
            for error in errors:
                print(error)
            for k in errors:
                messages.error(request, errors[k], extra_tags = k)
            return redirect("/login")
        else:
            request.session["isLoggedIn"] = True
            request.session["thisUserID"] = addUser(request.POST).id
            return redirect("/belt")

def success(request):
    if not request.session['isLoggedIn']:
        return redirect("/login")
    else:
        context = {
            "thisUser": User.objects.get(id = request.session["thisUserID"])
        }
        return render(request,'loginApp/index.html', context)

def logout(request):
    request.session['isLoggedIn'] = False
    request.session["thisUser"] = None
    return render(request, "loginApp/registration.html")

# TESTING PURPOSES
# def delete_users():
#         users = User.objects.all()
#         for use in users:
#                 user.delete()