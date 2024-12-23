import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "HERE SHOULD BE EMAIL"
    password = "HERE SHOULD BE YOUR PASSWORD"

    receiver = "HERE SHOULD BE EMAIL"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)