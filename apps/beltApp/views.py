##### Belt Exam - Belt App
##### Mason Brewer
##### November 19th, 2018

from django.shortcuts import render, redirect
from time import gmtime, strftime
import random, datetime, bcrypt
from .models import *
from django.contrib import messages
from apps.loginApp.models import User

# Home Page
def home(request):
    if not request.session['isLoggedIn']:
        return redirect("/login")
    else:
        thisUser = User.objects.get(id = request.session["thisUserID"])
        context = {
            "thisUser": thisUser,
            "notMyJobs": Job.objects.filter(volunteer=None),
            "myJobs": Job.objects.filter(volunteer=thisUser),
        }
        return render(request,'beltApp/home.html', context)

# New Job Page
def newJobPage(request):
    return render(request,'beltApp/new.html')

# New Job Process
def newJobProcess(request):
    if request.method == "GET":
        return redirect("/belt/job/new")
    if request.method == "POST":
        allCats = ""
        if "pet" in request.POST:
            allCats += request.POST["pet"] + " "
        if "electrical" in request.POST:
            allCats += request.POST["electrical"] + " "
        if "garden" in request.POST:
            allCats += request.POST["garden"] + " "
        allCats += request.POST["extraCategories"]
        errors = Job.objects.jobValidator(request.POST, allCats)
        if len(errors) > 0:
            for k in errors:
                messages.error(request, errors[k], extra_tags = k)
            return redirect("/belt/job/new")
        else:
            allCats = ""
            if "pet" in request.POST:
                allCats += request.POST["pet"] + " "
            if "electrical" in request.POST:
                allCats += request.POST["electrical"] + " "
            if "garden" in request.POST:
                allCats += request.POST["garden"] + " "
            allCats += request.POST["extraCategories"]
            thisUser = User.objects.get(id=request.session["thisUserID"])
            thisJob = Job.objects.create(title=request.POST["title"], decription=request.POST["description"], location=request.POST["location"], catergories=allCats, poster=thisUser)
            request.session["thisJobID"] = thisJob.id
            return redirect("/belt/job/view")

# Edit Job Page
def editJobPage(request):
    if request.method == "POST":
        request.session["thisJobID"] = request.POST["whichJob"]
    context = {
        "thisJob": Job.objects.get(id=request.session["thisJobID"])
    }
    return render(request,'beltApp/edit.html', context)

# Edit Job Process
def editJobProcess(request):
    if request.method == "GET":
        return redirect("/belt/job/edit")
    if request.method == "POST":
        errors = Job.objects.jobValidator(request.POST)
        if len(errors) > 0:
            for k in errors:
                messages.error(request, errors[k], extra_tags = k)
            return redirect("/belt/job/edit")
        else:
            thisJob = Job.objects.get(id=request.session["thisJobID"])
            thisJob.title = request.POST["title"]
            thisJob.decription = request.POST["description"]
            thisJob.location = request.POST["location"]
            thisJob.save()
            return redirect("/belt/job/view")

# Job Delete
def jobDelete(request):
    if request.method == "GET":
        return redirect("/belt")
    if request.method == "POST":
        thisJob = Job.objects.get(id=request.POST["whichJob"])
        thisJob.delete()
        return redirect("/belt")

# View Job Page
def viewJobPage(request):
    if request.method == "POST":
        request.session["thisJobID"] = request.POST["whichJob"]
    context = {
        "thisJob": Job.objects.get(id=request.session["thisJobID"])
    }
    return render(request,'beltApp/view.html', context)


# Adding Job to personal Roster
def jobAdd(request):
    if request.method == "GET":
        return redirect("/belt")
    if request.method == "POST":
        thisJob = Job.objects.get(id=request.POST["whichJob"])
        thisJob.volunteer = User.objects.get(id=request.session["thisUserID"])
        thisJob.save()
        return redirect("/belt")

# Removing Job to personal Roster
def jobRemove(request):
    if request.method == "GET":
        return redirect("/belt")
    if request.method == "POST":
        thisJob = Job.objects.get(id=request.POST["whichJob"])
        print(thisJob.title)
        thisJob.volunteer = None
        thisJob.save()
        return redirect("/belt")

# Completing the Job
def jobDone(request):
    if request.method == "GET":
        return redirect("/belt")
    if request.method == "POST":
        thisJob = Job.objects.get(id=request.POST["whichJob"])
        thisJob.delete()
        return redirect("/belt")