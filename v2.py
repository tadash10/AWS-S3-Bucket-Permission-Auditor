import boto3
from botocore.exceptions import BotoCoreError, NoCredentialsError

def scan_s3_bucket_permissions():
    try:
        # Initialize AWS S3 client
        s3_client = boto3.client('s3')

        # List all S3 buckets
        buckets = s3_client.list_buckets()

        # Initialize a list to store audit results
        audit_results = []

        # Iterate through each bucket
        for bucket in buckets.get('Buckets', []):
            bucket_name = bucket['Name']

            # Get bucket policy
            try:
                bucket_policy = s3_client.get_bucket_policy(Bucket=bucket_name)
                policy_statement = bucket_policy.get('Policy', '')

                # Check if the policy allows public access
                if 'Effect" : "Allow"' in policy_statement and 'Principal": "*"' in policy_statement:
                    audit_results.append({'Bucket': bucket_name, 'Status': 'Public Access Allowed'})
            except BotoCoreError as e:
                if 'NoSuchBucketPolicy' not in str(e):
                    print(f"Error getting bucket policy for {bucket_name}: {e}")

            # Get bucket ACL
            try:
                bucket_acl = s3_client.get_bucket_acl(Bucket=bucket_name)

                # Check if any grant allows public access
                for grant in bucket_acl.get('Grants', []):
                    grantee = grant.get('Grantee', {})
                    if 'URI' in grantee and 'http://acs.amazonaws.com/groups/global/AllUsers' in grantee.get('URI', ''):
                        audit_results.append({'Bucket': bucket_name, 'Status': 'Public Access Allowed'})
            except BotoCoreError as e:
                if 'NoSuchBucket' not in str(e):
                    print(f"Error getting bucket ACL for {bucket_name}: {e}")

        return audit_results
    except NoCredentialsError:
        print("AWS credentials are missing or invalid.")
        return []

def main():
    audit_results = scan_s3_bucket_permissions()

    if audit_results:
        print("S3 Bucket Permission Audit Results:")
        for result in audit_results:
            print(f"Bucket: {result['Bucket']}, Status: {result['Status']}")
    else:
        print("No issues found. All S3 bucket permissions are properly configured.")

if __name__ == "__main__":
    main()
