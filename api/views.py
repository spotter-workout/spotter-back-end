from rest_framework.views import APIView
from django.http import JsonResponse


class HelloWorld(APIView):
    def get(self, request):
        return JsonResponse("Hello World!", safe=False)
