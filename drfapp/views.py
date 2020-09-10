from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response


class UserAPIView(APIView):
    def get(self, request, *args, **kwargs):
        print('get请求')
        return Response('drf get ok')