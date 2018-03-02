import boto3

class QueueController(object):

    def __init__(self):
        session = boto3.Session(profile_name='python-scripts')
        self.sqsClient = session.client('sqs', region_name='us-east-1')

    def ReadMessages(self, queueUrl):
        messageResponse = self.sqsClient.receive_message(
            QueueUrl = queueUrl,
            MaxNumberOfMessages = 1
        )        
        return messageResponse

    def GetEmailAddress(self, message):
        body = msg['Messages'][0]['Body']
        emailAddressIndex = body.find('emailAddress')
        emailString = body[emailAddressIndex:emailAddressIndex+100].replace('\\"', '') 
        emailAddress = emailString.split(',')
        return emailAddress[0].split(':')[1]

q = QueueController()
msg = q.ReadMessages("https://sqs.us-east-1.amazonaws.com/498566610564/email-bounces")
emailAddress = q.GetEmailAddress(msg)
print(emailAddress)
