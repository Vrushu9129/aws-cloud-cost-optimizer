
import boto3

REGION = "ap-south-1"

ec2 = boto3.client("ec2", region_name=REGION)

print("\nAWS EBS COST OPTIMIZATION REPORT")
print("--------------------------------")

response = ec2.describe_volumes(
    Filters=[
        {"Name": "status", "Values": ["available"]}
    ]
)

volumes = response["Volumes"]

if not volumes:
    print("No unattached EBS volumes found.")
else:
    for volume in volumes:
        print("\nVolume ID:", volume["VolumeId"])
        print("Size:", volume["Size"], "GB")
        print("Type:", volume["VolumeType"])
        print("Status:", volume["State"])
        print("Recommendation: Review this unused volume.")
        print("Delete only after verifying its data is not needed.")
