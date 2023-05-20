import smtplib
from email.message import EmailMessage
#if forecast[0] != forecast [1]
# Open the plain text file whose name is in textfile for reading.
with open('C:Users/jq/Documents/WeatherForecast/email.txt', 'rb') as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(fp.read())

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = f'The contents of {textfile}'
msg['From'] = me
msg['To'] = whenthecurtainrises@gmail.com

# Send the message via our own SMTP server.
sendit = smtplib.SMTP('localhost')
sendit.send_message(msg)
sendit.quit()