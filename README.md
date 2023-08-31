# AWS-S3-Bucket-Permission-Auditor


The S3 Bucket Permission Auditor is a Python script that helps you identify AWS S3 buckets with open or improperly configured access policies. This can assist in enhancing the security of your S3 resources by detecting potential vulnerabilities.

## Installation

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/your-username/s3-bucket-permission-auditor.git
   cd s3-bucket-permission-auditor

Install the required dependencies using pip:
pip install -r requirements.txt


Usage

    Make sure you have configured your AWS credentials using the AWS CLI or environment variables.

    Open a terminal and navigate to the s3-bucket-permission-auditor directory.

    Run the script using the following command:

python main_script.py


    The script will start auditing your S3 buckets and display the results in the terminal. It will identify buckets with open or improperly configured access policies.

Functions

The script is organized into several utility functions:

    get_s3_client(): Initializes the AWS S3 client and handles AWS credential errors.
    list_s3_buckets(s3_client): Lists all S3 buckets.
    get_bucket_policy(s3_client, bucket_name): Retrieves the bucket policy for a given bucket.
    get_bucket_acl(s3_client, bucket_name): Retrieves the ACL grants for a given bucket.
    scan_bucket_permissions(bucket): Scans a bucket for public access permissions.

Notes

    The script uses the AWS SDK (boto3) for Python to interact with AWS services. Ensure your AWS credentials are correctly configured for the script to work.
    This script provides a basic level of security auditing. Make sure to review and adapt it according to your organization's security policies and requirements.
    Always test the script in a controlled environment before running it on production resources.

License

This project is licensed under the MIT License.

