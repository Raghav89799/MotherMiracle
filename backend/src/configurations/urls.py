from django.urls import path
from .views import *

urlpatterns = [
    path('login/',LoginView.as_view(),name="login"),
    path('register/',RegisterView.as_view(),name="register"),
    path('register/<int:pk>/',RegisterView.as_view(),name="register"),
]