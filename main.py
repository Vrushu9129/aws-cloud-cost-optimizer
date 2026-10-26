
import boto3
from botocore.exceptions import BotoCoreError, ClientError, NoCredentialsError

REGION = "ap-south-1"
BUCKET_NAME = "cost-optimiser-demo"

ec2 = boto3.client("ec2", region_name=REGION)
s3 = boto3.client("s3")

print("\nAWS DEVOPS COST OPTIMIZER")
print("--------------------------")

try:
    # Read EC2 instances
    response = ec2.describe_instances()

    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            print(
                "EC2 Instance:", instance["InstanceId"],
                "| State:", instance["State"]["Name"],
                "| Type:", instance["InstanceType"]
            )

    # Read S3 objects
    response = s3.list_objects_v2(Bucket=BUCKET_NAME)

    total_size = 0

    for obj in response.get("Contents", []):
        print("S3 Object:", obj["Key"], "| Bytes:", obj["Size"])
        total_size += obj["Size"]

    print("S3 total listed size:", total_size, "bytes")
    print("\nAWS resource collection completed!")

except (BotoCoreError, ClientError, NoCredentialsError) as error:
    print("AWS connection or permission error:", error)
