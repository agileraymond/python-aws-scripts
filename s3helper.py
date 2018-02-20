import boto3

session = boto3.Session(profile_name='python-scripts')
s3 = session.client('s3')

filename = 'test.txt'
bucket_name = 'mysql-emails'

# read csv file from mysql-emails bucket
