import smtplib, ssl

def emailSend(sender_email, receiver_email, message):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login("tt2249110@gmail.com", 'grac1e11')
        server.sendmail(sender_email, receiver_email, message)

