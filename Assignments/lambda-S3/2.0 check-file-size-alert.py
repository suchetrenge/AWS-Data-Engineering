import logging
import boto3

# Set logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)


# S3 client
s3 = boto3.client('s3')

# Threshold in bytes (100 MB)
SIZE_THRESHOLD = 100 * 1024 * 1024

def lambda_handler(event, context):
    print("event : ",event)
    event :  {'Records': [{'eventVersion': '2.1', 'eventSource': 'aws:s3', 'awsRegion': 'us-east-1', 'eventTime': '2025-06-04T15:00:21.205Z', 'eventName': 'ObjectCreated:Put', 'userIdentity': {'principalId': 'A1VI7QNM23AJE5'}, 'requestParameters': {'sourceIPAddress': '49.43.231.246'}, 'responseElements': {'x-amz-request-id': 'P69WWE9CWXSTF3W7', 'x-amz-id-2': 'VF5doc6Kl+Sl/NhvxX8LZAgpgmjfrLCfcaY5sw0yF9M4WHMcf6OJtxtiK3Vd0nTduRby17Owb0fq0ve6yOs6DCNiyworwYlj'}, 's3': {'s3SchemaVersion': '1.0', 'configurationId': 'dbd3ce29-eae3-4103-8a5d-0018be91e336', 'bucket': {'name': 'aws-de-s3-bucket-1807', 'ownerIdentity': {'principalId': 'A1VI7QNM23AJE5'}, 'arn': 'arn:aws:s3:::aws-de-s3-bucket-1807'}, 'object': {'key': 'assignment_data/AWS_Lambda_Assignment_1.pdf', 'size': 215293, 'eTag': '8d58f865b94ef2da0ac8a27703968211', 'sequencer': '0068405F851B11F963'}}}]}
    for record in event['Records']:
        bucket_name = record['s3']['bucket']['name']
        object_key = record['s3']['object']['key']
        
        logger.info(f"Processing file: s3://{bucket_name}/{object_key}")

        key_size = record['s3']['object']['size']
        
        # Get object metadata
        response = s3.head_object(Bucket=bucket_name, Key=object_key)
        file_size = response['ContentLength']
        
        print("file_size : ",file_size)
        print("key_size : ",_siz)
        
        if key_size > SIZE_THRESHOLD:
            logger.warning(f"⚠️ Alert: File '{object_key}' in bucket '{bucket_name}' is {file_size / (1024*1024):.2f} MB — exceeds 100 MB limit.")
        else:
            logger.info(f"✅ File '{object_key}' is within size limits: {file_size / (1024*1024):.2f} MB.")

        
    
    
