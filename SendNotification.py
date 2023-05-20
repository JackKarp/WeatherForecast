from plyer import notification

def SendNotification(type, forecast):
    if type == 1:
        notification.notify(
            title = 'Weather Change!',
            message = 'The weather has changed from ' + forecast[0] + ' to ' + forecast[1],
            app_icon = './icon_final.ico',
            timeout = 20,
        )
    if type == 2:
        notification.notify(
            title = 'Rain Incoming!',
            message = forecast + '% chance of rain',
            app_icon = './icon_final.ico',
            timeout = 20,
        )
    if type == 3:
        notification.notify(
            title = 'Current Weather',
            message = forecast,
            app_icon = './icon_final.ico',
            timeout = 20,
        )

