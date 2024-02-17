from django.urls import path
from . import views


urlpatterns = [
    path('main/', views.main, name='Главная страница'),
    path('myapp/', views.myapp, name='О себе'),

]