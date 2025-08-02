import boto3
from datetime import datetime, timezone

def terminate_latest_instance():
    ec2 = boto3.client('ec2', region_name='ap-south-1')

    # Describe running instances
    response = ec2.describe_instances(
        Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
    )

    # Debugging: Print the response to see all the instances
    print("Response:", response)

    latest_instance = None
    latest_launch_time = None

    # Find the most recently launched running instance
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            launch_time = instance['LaunchTime']
            print(f"Instance {instance['InstanceId']} launched at {launch_time}")
            if latest_launch_time is None or launch_time > latest_launch_time:
                latest_instance = instance
                latest_launch_time = launch_time

    if latest_instance:
        instance_id = latest_instance['InstanceId']
        print(f"Terminating most recent instance: {instance_id}")
        ec2.terminate_instances(InstanceIds=[instance_id])
    else:
        print("No running instances found.")

if __name__ == "__main__":
    terminate_latest_instance()
