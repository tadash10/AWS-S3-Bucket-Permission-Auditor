import boto3
from botocore.exceptions import ClientError

def scan_s3_bucket_permissions():
    # Initialize AWS S3 client
    s3_client = boto3.client('s3')

    # List all S3 buckets
    try:
        buckets = s3_client.list_buckets()
    except ClientError as e:
        print(f"Error listing buckets: {e}")
        return []

    # Initialize a list to store audit results
    audit_results = []

    # Iterate through each bucket
    for bucket in buckets['Buckets']:
        bucket_name = bucket['Name']
        
        # Get bucket policy
        try:
            bucket_policy = s3_client.get_bucket_policy(Bucket=bucket_name)
            policy_statement = bucket_policy['Policy']
            
            # Check if the policy allows public access
            if 'Effect" : "Allow"' in policy_statement and 'Principal": "*"' in policy_statement:
                audit_results.append({'Bucket': bucket_name, 'Status': 'Public Access Allowed'})
        except ClientError as e:
            if e.response['Error']['Code'] == 'NoSuchBucketPolicy':
                pass  # No bucket policy
            else:
                print(f"Error getting bucket policy for {bucket_name}: {e}")

        # Get bucket ACL
        try:
            bucket_acl = s3_client.get_bucket_acl(Bucket=bucket_name)
            
            # Check if any grant allows public access
            for grant in bucket_acl['Grants']:
                if 'URI' in grant['Grantee'] and 'http://acs.amazonaws.com/groups/global/AllUsers' in grant['Grantee']['URI']:
                    audit_results.append({'Bucket': bucket_name, 'Status': 'Public Access Allowed'})
        except ClientError as e:
            if e.response['Error']['Code'] == 'NoSuchBucket':
                pass  # Bucket doesn't exist or access denied
            else:
                print(f"Error getting bucket ACL for {bucket_name}: {e}")

    return audit_results

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
