from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from userapp.models import User


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


class EmployeeView(View):
    def get(self, request, *args, **kwargs):
        # user_id = request.GET.get('id')
        id = kwargs.get('id')
        print(id)
        if id:
            user = User.objects.filter(pk=id).values('username', 'password', 'gender', 'email').first()
            # user = User.objects.filter(pk=id)[0]
            if user:
                return JsonResponse({
                    'status': 200,
                    'message': '成功查询',
                    'results': user
                })
            else:
                return JsonResponse({
                    "status": 500,
                    "message": "查询用户不存在",
                })
        else:
            users = User.objects.all().values('username', 'password', 'gender', 'email')
            return JsonResponse({
                'status': 200,
                'message': '成功查询',
                'results': list(users)
            })


