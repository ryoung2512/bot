import smtplib
import sys

sender = "serenabotv1@gmail.com"
password = "g00b3r1f1c"


def send_message(message, email):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, email, message)
        server.quit()
        print('Successfully sent the message')
    except:
        print("Failed to send message exited with error code:", sys.exc_info()[0])


def get_email(country, provider):
    f = open("providers.txt", "r")
    email = ""
    for line in f:
        split_line = line.strip().split(", ")
        if (split_line[0].lower() == country.lower()) and split_line[1].lower().find(provider.lower()) != -1:
            email = split_line[2].split("@")
            break
    f.close()
    if email != "":
        return email[1]
    return email

email_out = "7173177329" + "@" + get_email("united states", "at&t")
send_message("test", email_out)
