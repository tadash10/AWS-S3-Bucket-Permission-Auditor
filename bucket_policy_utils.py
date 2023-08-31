from botocore.exceptions import BotoCoreError

def get_bucket_policy(s3_client, bucket_name):
    try:
        response = s3_client.get_bucket_policy(Bucket=bucket_name)
        return response.get('Policy', '')
    except BotoCoreError as e:
        if 'NoSuchBucketPolicy' not in str(e):
            print(f"Error getting bucket policy for {bucket_name}: {e}")
        return ''
