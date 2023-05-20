from plyer import notification
notification.notify(
    title = 'Weather Change!',
    message = 'The weather has changed from' + forecasts[0] + 'to' + forecasts[1],
    app_icon = None,
    timeout = 10,
)