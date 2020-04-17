from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
def index(request,arg):
    return JsonResponse({"msg":"OK","arg":arg})

def detail(request,question_id):
    return JsonResponse({"msg":"OK","arg":question_id})

def year(request,year_data):
    return JsonResponse({"msg":"OK","arg":year_data})