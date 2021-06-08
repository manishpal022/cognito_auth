import os
import boto3
from dotenv import load_dotenv

load_dotenv()

username = 'manishpal.055@gmail.com'
confirm_code = '256025'
password = 'Mani@321'

client = boto3.client('cognito-idp', region_name=os.getenv('COGNITO_REGION_NAME'))
response = client.confirm_forgot_password(
    ClientId = os.getenv('COGNITO_USER_CLIENT_ID'),
    Username = username,
    ConfirmationCode = confirm_code,
    Password = password
)

print(response)