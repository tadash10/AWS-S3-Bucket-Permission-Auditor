from s3_client_utils import get_s3_client
from list_buckets_utils import list_s3_buckets
from bucket_policy_utils import get_bucket_policy
from bucket_acl_utils import get_bucket_acl
from scan_permissions_utils import scan_bucket_permissions
from botocore.exceptions import BotoCoreError

def main():
    s3_client = get_s3_client()
    if not s3_client:
        return

    buckets = list_s3_buckets(s3_client)
    if not buckets:
        print("No buckets found.")
        return

    audit_results = []
    for bucket in buckets:
        audit_results.extend(scan_bucket_permissions(bucket))

    if audit_results:
        print("S3 Bucket Permission Audit Results:")
        for result in audit_results:
            print(f"Bucket: {result['Bucket']}, Status: {result['Status']}")
    else:
        print("No issues found. All S3 bucket permissions are properly configured.")

if __name__ == "__main__":
    main()
