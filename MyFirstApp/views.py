from django.shortcuts import render
from django.http.response import JsonResponse

def FirstApp(request):
    responseData = {
        'message': "Hello World"
        
    }

    return JsonResponse(responseData)
