from django.shortcuts import render
# from django.core.mail import EmailMessage, BadHeaderError
# from templated_mail.mail import BaseEmailMessage
# from django.conf import settings
# import os
from playground.tasks import notify_customers
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from django.utils.decorators import method_decorator

import requests


@cache_page(2*60)
def say_hello(request):
    response = requests.get('https://httpbin.org/delay/2')
    data = response.json()
    return render(request, 'hello.html', {'name': data})


# class TestingCache(APIView):
#     @method_decorator(cache_page(5*60))
#     def get(self, request):
#         pass
