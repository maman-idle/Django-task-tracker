from django.urls import path
from . import views

urlpatterns = [
    path('', views.Login, name='login'),
    path('login/', views.Login, name='login'),
    path('signup/', views.SignUp, name='signup')
]