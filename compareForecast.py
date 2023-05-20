import json
import os

with open('C:/Users/jacka/Documents/WeatherForecast/forecastValues.txt', 'r') as forecastval:
    forecast = forecastval.read().split('*')
    if forecast[0] != forecast[1]:
        #do thing
        print('yeet')
    else:
        print(forecastval.read())