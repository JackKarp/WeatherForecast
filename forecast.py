from urllib.request import urlopen
import json
import os

from SendNotification import SendNotification

url = "https://api.weather.gov/points/32.7157,-117.1611"
  
# store the response of URL
response = urlopen(url)
  
# storing the JSON response 
# from url in data
data_json = json.loads(response.read())
  
# print the json response
#print(data_json)

#parse to forecast
forecastlink = data_json['properties']['forecast']

#pull json from weather.gov
fullforecast = urlopen(forecastlink)
data_forecast = json.loads(fullforecast.read())

shortForecast = str(data_forecast['properties']['periods'].pop(0)['shortForecast'])
forecast = []

#set old value to forecast
with open('./forecastValues.txt', 'r') as forecastval:
    forecast = forecastval.read().split('*')
    while len(forecast) > 1:
        forecast.pop(0)

#send new value to file
with open('./forecastValues.txt', 'w') as forecastval:
    forecast.append(shortForecast)
    print(forecast)
    if len(forecast) == 1:
        forecastval.write(shortForecast)
    else:
        forecastval.write(forecast[0]+'*'+forecast[1])

#compare old and new and run send notification
with open('./forecastValues.txt', 'r') as forecastval:
    forecast = forecastval.read().split('*')
    if forecast[0] != forecast[1]:
        SendNotification(forecast)
    else:
        print(forecastval.read())



#==========================RAIN TEST===============================

print(forecastlink)

rainForcast = str(data_forecast['properties']['periods'].pop(0)['probabilityOfPrecipitation']['value'])
print(rainForcast)
try:
    if int(rainForcast) > 70:
        SendNotification(rainForcast)
except ValueError:
    print('')