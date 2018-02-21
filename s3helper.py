import boto3
from EmailController import EmailController

filename = 'testemails.csv'
bucket_name = 'mysql-emails'

file = open(filename, 'r')
emailer = EmailController()

fromAddress = ''
toAddress = ''
subject = 'updates from solutionsByRaymond.com'
emailBody = "<p>Hi, I'm Raymond, founder of solutionsByRaymond.com.</p>"

for line in file:
    response = emailer.SendEmail(fromAddress, toAddress, subject, emailBody)
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        print('success')
    else:
        print('failed')
    