from xml.dom.minidom import TypeInfo
from .models import Greeting
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
import requests
from django import forms
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import json
from mgz.model import parse_match, serialize


def handle_uploaded_file(f):
    match = parse_match(f)
    print(type(match))
    return match


@csrf_exempt
def handlefile(request):
    if request.method == 'POST':
        if len(request.FILES) == 1:
            jsondata = handle_uploaded_file(request.FILES['file'])
            res = HttpResponse(
                jsondata, {'Content-Type': 'application/json'}, 200)
            return res
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


@csrf_exempt
def getInputs(request):
    if request.method == 'POST':
        if len(request.FILES) == 1:
            jsondata = handle_uploaded_file(request.FILES['file'])
            resdata = jsondata.inputs
            res = HttpResponse(
                resdata, {'Content-Type': 'application/json'}, 200)
            return res
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


def getActions(request):
    if request.method == 'POST':
        if len(request.FILES) == 1:
            jsondata = handle_uploaded_file(request.FILES['file'])
            resdata = jsondata.actions
            res = HttpResponse(
                resdata, {'Content-Type': 'application/json'}, 200)
            return res
        else:
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/')


@csrf_protect
def index(request):
    return render(request, 'index.html')


# Create your views here.


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
