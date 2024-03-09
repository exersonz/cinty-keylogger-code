import smtplib, ssl

def sendEmail(message):
    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "iamthedummydummy@gmail.com"
    password = "Iamthedummy$"
    receiver_email = "cinty.lin.cinty@gmail.com"
    context = ssl.create_default_context()

    try:
        server = smtplib.SMTP(smtp_server, port)
        # an email client can inform the email server that it wants to upgrade from insecure to secure connection using tls
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendemail(sender_email, receiver_email, message)
    except Exception as e:
        print(e)
    finally:
        server.quit()