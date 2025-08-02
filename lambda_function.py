import boto3
import json
from datetime import datetime

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    
    bucket_name = 'group20-ec2-logs-bucket'  # <--- Make sure it is exact
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    instance_id = event['detail'].get('instance-id', 'unknown-instance')
    state = event['detail'].get('state', 'unknown-state')
    
    log_content = json.dumps({
        'instance_id': instance_id,
        'state': state,
        'timestamp': timestamp
    })
    
    object_key = f'logs/{instance_id}_{timestamp}.json'
    
    s3.put_object(Bucket=bucket_name, Key=object_key, Body=log_content)
    
    return {
        'statusCode': 200,
        'body': 'Saved event to S3'
    }
