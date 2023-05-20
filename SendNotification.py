from plyer import notification

def SendNotification(list forecasts):
    notification.notify(
        title = 'Weather Change!',
        message = 'The weather has changed from' + forecasts[0] + 'to' + forecasts[1],
        app_icon = None,
        timeout = 10,
    )