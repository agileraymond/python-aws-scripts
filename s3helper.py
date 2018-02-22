import boto3
from EmailController import EmailController

filename = 'emails.csv'
bucket_name = 'mysql-emails'

file = open(filename, 'r')
emailer = EmailController()

fromAddress = 'agileraymond@gmail.com'
subject = 'updates from solutionsByRaymond.com'

emailBody = """<p>Hi, I'm Raymond, founder of solutionsByRaymond.com. I just want to share my latest articles via email.</p>
    <p>Here you go: </p>
    <ul>
        <li><a href="http://solutionsbyraymond.com/2018/01/08/creating-aws-codedeploy-application-using-net-sdk/">
            Creating AWS CodeDeploy Application Using .NET SDK</a></li>
        <li><a href="http://solutionsbyraymond.com/2018/01/22/creating-aws-codedeploy-deployment-groups-using-net-sdk/">
            Creating AWS CodeDeploy Deployment Groups Using .NET SDK</a></li>
        <li><a href="http://solutionsbyraymond.com/2018/02/06/creating-aws-codedeploy-deployments-using-net-sdk/">
            Creating AWS CodeDeploy Deployments Using .NET SDK</a></li>    
    </ul>
    <p>Have a good day!
    </p>    
    """

emailErrors = open('emailErrors.txt', 'w')

for toEmail in file:
    print('start sending email to: {}'.format(toEmail))
    try:
        response = emailer.SendEmail(fromAddress, toEmail, subject, emailBody)
        if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
            print('success')
        else:
            emailErrors.write(toEmail)
    except:
        emailErrors.write('exception: {}'.format(toEmail))

emailErrors.close()