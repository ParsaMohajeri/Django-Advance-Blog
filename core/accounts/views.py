from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from time import sleep
from .tasks import sendEmail
import requests
# __________________________

def send_email(request):
    sendEmail.delay()
    return HttpResponse("<h1> Done Sending</h1>")

@cache_page(60)
def test(request):
    response =requests.get("https://e2805c1f-8652-4d18-b5b2-3b0d732bbd34.mock.pstmn.io/test/delay/5")
    return JsonResponse(response.json())