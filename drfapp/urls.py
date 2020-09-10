from django.urls import path

from drfapp import views

urlpatterns = [
    path('drf_user/', views.UserAPIView.as_view()),
]