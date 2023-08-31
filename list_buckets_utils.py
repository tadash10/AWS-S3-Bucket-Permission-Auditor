from botocore.exceptions import BotoCoreError

def list_s3_buckets(s3_client):
    try:
        response = s3_client.list_buckets()
        return response.get('Buckets', [])
    except BotoCoreError as e:
        print(f"Error listing buckets: {e}")
        return []
