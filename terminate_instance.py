import boto3

def terminate_instance(instance_id):
    ec2 = boto3.client('ec2')
    try:
        response = ec2.terminate_instances(InstanceIds=[instance_id])
        print(f"Terminating instance: {instance_id}")
        print(response)
    except Exception as e:
        print(f"Error: {e}")

terminate_instance('i-079a538363427a896')
