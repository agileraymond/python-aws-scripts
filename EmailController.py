import boto3

class EmailController(object):

    def __init__(self):
        session = boto3.Session(profile_name='python-scripts')
        self.emailClient = session.client('ses', region_name='us-east-1')

    def SendEmail(self, fromAddress, toAddress, subject, emailBody):    
        response = self.emailClient.send_email(
        Source = fromAddress,
        Destination={
            'ToAddresses': [
                toAddress,
            ]
        },
        Message={
            'Subject': {
                'Data': subject,
                'Charset': 'UTF-8'
            },
            'Body': {
                'Text': {
                    'Data': emailBody,
                    'Charset': 'UTF-8'
                },
                'Html': {
                    'Data': emailBody,
                    'Charset': 'UTF-8'
                }
            }
        },
        ConfigurationSetName='test'
        )
        return response