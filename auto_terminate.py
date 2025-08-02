import time
import boto3

INSTANCE_ID = "i-06b25838c7b05c10f"
REGION = "ap-south-1"

ec2 = boto3.client("ec2", region_name=REGION)

def start_countdown():
    print("Instance will be terminated in:")
    for i in range(20, -1, -1):
        print(f"\r{i} seconds remaining...", end="", flush=True)
        time.sleep(1)
    print("\nInstance automatically terminating...")
    try:
        response = ec2.terminate_instances(InstanceIds=[INSTANCE_ID])
        print(f"Instance {INSTANCE_ID} termination request sent.")
    except Exception as e:
        print(f"Error terminating instance: {e}")

start_countdown()
