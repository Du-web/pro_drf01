from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login(request):
    if request.method == 'GET':
        print(request.GET.get('username'))
        return HttpResponse('GET,访问成功')
    if request.method == 'POST':
        print(request.POST.get('username'))
        return HttpResponse('POST,访问成功')
    if request.method == 'PUT':
        print(request.GET.get('username'))
        return HttpResponse('PUT,更新成功')
    if request.method == 'DELETE':
        print(request.GET.get('username'))
        return HttpResponse('DELETE,删除成功')

@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):
    def get(self, request, *args, **kwargs):
        print('GET请求')
        return HttpResponse('GET, 请求成功')

    def post(self, request, *args, **kwargs):
        print('POST请求')
        return HttpResponse('POST, 请求成功')

    def put(self, request, *args, **kwargs):
        print('PUT请求')
        return HttpResponse('PUT, 请求成功')

    def delete(self, request, *args, **kwargs):
        print('DELETE请求')
        return HttpResponse('DELETE, 请求成功')
