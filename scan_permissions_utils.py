from bucket_policy_utils import get_bucket_policy
from bucket_acl_utils import get_bucket_acl
from botocore.exceptions import BotoCoreError

def scan_bucket_permissions(bucket):
    s3_client = get_s3_client()
    if not s3_client:
        return []

    bucket_name = bucket['Name']
    policy_statement = get_bucket_policy(s3_client, bucket_name)
    acl_grants = get_bucket_acl(s3_client, bucket_name)

    audit_results = []

    # Check bucket policy
    if 'Effect" : "Allow"' in policy_statement and 'Principal": "*"' in policy_statement:
        audit_results.append({'Bucket': bucket_name, 'Status': 'Public Access Allowed (Policy)'})

    # Check ACL grants
    for grant in acl_grants:
        grantee = grant.get('Grantee', {})
        if 'URI' in grantee and 'http://acs.amazonaws.com/groups/global/AllUsers' in grantee.get('URI', ''):
            audit_results.append({'Bucket': bucket_name, 'Status': 'Public Access Allowed (ACL)'})

    return audit_results
