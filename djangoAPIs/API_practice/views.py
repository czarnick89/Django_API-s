from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import os

# Create your views here.
class DefaultView(APIView):
    def get(self, response):
        return Response('check this')
    
class WeatherView(APIView):

    def get(self,response, city):

        api_url = f'http://api.weatherstack.com/current?access_key={os.environ.get('WEATHER_API_KEY')}&query={city}'
        #print(api_url)
        response = requests.get(api_url)
        responseJSON = response.json()
        return Response(responseJSON)

class StockView(APIView):

    def get(self,response, ticker):

        api_url = f'http://api.marketstack.com/v1/eod?access_key={os.environ.get('STOCK_API_KEY')}&symbols={ticker}'
        #print(api_url)
        response = requests.get(api_url)
        responseJSON = response.json()
        return Response(responseJSON)
    
class WorkoutView(APIView):
    
    def get(self, response, id):
        api_url=f'https://exercisedb.p.rapidapi.com/exercises/exercise/{id}'

        headers = {
            "x-rapidapi-key": os.environ.get('EXERCISE_RAPIDAPI_KEY'),
            "x-rapidapi-host": "exercisedb.p.rapidapi.com"
            }

        response = requests.get(api_url, headers=headers)

        return Response(response.json())
    
class YelpView(APIView):

    def get(self, response, query):
        url = "https://yelp-scraper1.p.rapidapi.com/api/business/info"

        querystring = {"alias":query}

        headers = {
            "x-rapidapi-key": os.environ.get('EXERCISE_RAPIDAPI_KEY'),
            "x-rapidapi-host": "yelp-scraper1.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        data = response.json()

        return Response(data)