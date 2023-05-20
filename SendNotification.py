from plyer import notification

def SendNotification(forecast):
    notification.notify(
        title = 'Weather Change!',
        message = 'The weather has changed from ' + forecast[0] + ' to ' + forecast[1],
        app_icon = None,
        timeout = 10,
    )
    print('georg')

