import boto3
from datetime import datetime, timezone, timedelta

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    BUCKET_NAME = "s3-auto-cleanup-demo-r"
    MINUTES_OLD = 2  # Delete files older than 2 minutes (for testing)

    cutoff_time = datetime.now(timezone.utc) - timedelta(minutes=MINUTES_OLD)

    response = s3.list_objects_v2(Bucket=BUCKET_NAME)

    if 'Contents' not in response:
        print("Bucket is empty")
        return {
            'statusCode': 200,
            'body': 'Bucket is empty, nothing to delete'
        }

    deleted_files = []

    for obj in response['Contents']:
        if obj['LastModified'] < cutoff_time:
            s3.delete_object(
                Bucket=BUCKET_NAME,
                Key=obj['Key']
            )
            deleted_files.append(obj['Key'])

    if deleted_files:
        print("Deleted files:")
        for file in deleted_files:
            print(file)
    else:
        print("No files older than 2 minutes found")

    return {
        'statusCode': 200,
        'body': 'S3 cleanup executed successfully'
    }
