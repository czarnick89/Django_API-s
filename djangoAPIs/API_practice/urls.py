from django.urls import path, include
from .views import *

urlpatterns = [
    path('', DefaultView.as_view(), name='default'),
    path('weather/<str:city>', WeatherView.as_view()),
    path('stocks/<str:ticker>', StockView.as_view()),
    path('exercise/<str:id>', WorkoutView.as_view()),
    path('yelp/<str:query>', YelpView.as_view()),
    ]