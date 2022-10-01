from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
def json_name(request):
    return JsonResponse({"Name": "Hello World!"})
