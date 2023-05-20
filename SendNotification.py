from plyer import notification

def SendNotification(forecast):
    if type(forecast) == list:
        notification.notify(
            title = 'Weather Change!',
            message = 'The weather has changed from ' + forecast[0] + ' to ' + forecast[1],
            app_icon = './icon_final.ico',
            timeout = 20,
        )
    if type(forecast) == str:
        notification.notify(
            title = 'Rain Incoming!',
            message = forecast + '% chance of rain',
            app_icon = './icon_final.ico',
            timeout = 20,
        )
    print('georg')

