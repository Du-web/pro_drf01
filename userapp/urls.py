from django.urls import path

from userapp import views

urlpatterns = [
    path('/login', views.login),
    path('/userview', views.UserView.as_view()),
]
