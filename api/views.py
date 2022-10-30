from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

class HelloWorld(APIView):
    def get(self, request):
        return JsonResponse("Hello World!", safe=False)


