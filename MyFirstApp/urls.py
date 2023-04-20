from django.urls import path
from . import views

urlpatterns = [
    path('',views.FirstApp, name='FirstApp')
]