import smtplib

sender_email = str(input("Enter your email: "))
recipient_email = str(input("Enter the recipient's email: "))
password = input("Enter your password: ")

Message = """\
        Hi there
        Subject: MASENO APPLICATION

        send from iphone using Python."""

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
server.sendmail(sender_email, recipient_email, Message)
print("Email was sent successfully")


