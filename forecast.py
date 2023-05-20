from urllib.request import urlopen
import json
import os

url = "https://api.weather.gov/points/32.7432,-117.1736"
  
# store the response of URL
response = urlopen(url)
  
# storing the JSON response 
# from url in data
data_json = json.loads(response.read())
  
# print the json response
#print(data_json)

#parse to forecast
forecastlink = data_json['properties']['forecast']

#print(forecastlink)
fullforecast = urlopen(forecastlink)
data_forecast = json.loads(fullforecast.read())

shortForecast = str(data_forecast['properties']['periods'].pop(0)['shortForecast'])
forecast = []

#forecastval = open('C:/Users/jacka/Documents/WeatherForecast/forecastValues.txt', 'w+')
with open('C:/Users/jacka/Documents/WeatherForecast/forecastValues.txt', 'r') as forecastval:
    forecast = forecastval.read().split('*')
    while len(forecast) > 1:
        forecast.pop(0)

with open('C:/Users/jacka/Documents/WeatherForecast/forecastValues.txt', 'w') as forecastval:
    forecast.append(shortForecast)
    print(forecast)
    if len(forecast) == 1:
        forecastval.write(shortForecast)
    else:
        forecastval.write(forecast[0]+'*'+forecast[1])



#compare old and new
with open('C:/Users/jacka/Documents/WeatherForecast/forecastValues.txt', 'r') as forecastval:
    forecast = forecastval.read().split('*')
    if forecast[0] != forecast[1]:
        #do thing
        print('yeet')
    else:
        print(forecastval.read())