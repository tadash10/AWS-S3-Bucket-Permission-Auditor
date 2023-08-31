import boto3
from botocore.exceptions import NoCredentialsError

def get_s3_client():
    try:
        return boto3.client('s3')
    except NoCredentialsError:
        print("AWS credentials are missing or invalid.")
        return None
