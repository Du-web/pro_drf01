from django.urls import path

from userapp import views

urlpatterns = [
    path('login/', views.login),
    path('userview/', views.UserView.as_view()),
    path('employeeview/<str:id>/', views.EmployeeView.as_view()),
    path('employeeview/', views.EmployeeView.as_view()),
]
