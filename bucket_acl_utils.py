from botocore.exceptions import BotoCoreError

def get_bucket_acl(s3_client, bucket_name):
    try:
        response = s3_client.get_bucket_acl(Bucket=bucket_name)
        return response.get('Grants', [])
    except BotoCoreError as e:
        if 'NoSuchBucket' not in str(e):
            print(f"Error getting bucket ACL for {bucket_name}: {e}")
        return []
