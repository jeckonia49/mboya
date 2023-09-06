
# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='mboyacleanio@gmail.com',
    to_emails=['jeckonia23@gmail.com',],
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
sg = SendGridAPIClient("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")
response = sg.send(message)
print(response.status_code)
# print(response.body)
# print(response.headers)



# class Main(object):
#     def __init__(self) -> None:
#         self.recipient_list = []
#     def send(subject, message, recipient):
#         sd = SendGridAPIClient(os.environ.get('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'))
#         sd.send()