from django.http import JsonResponse
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')

def ping(request, num:int=None):
    if num is None:
        return JsonResponse({
            'message': 'pong'
        })
    return JsonResponse({
        'message': 'pong' * num
    })