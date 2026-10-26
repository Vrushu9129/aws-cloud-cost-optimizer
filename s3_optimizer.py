
import boto3
from datetime import datetime, timezone

BUCKET_NAME = "cost-optimiser-demo"
AGE_THRESHOLD_DAYS = 30

s3 = boto3.client("s3", region_name="ap-south-1")

print("\nAWS S3 COST OPTIMIZATION REPORT")
print("--------------------------------")

total_size = 0
total_objects = 0

paginator = s3.get_paginator("list_objects_v2")

for page in paginator.paginate(Bucket=BUCKET_NAME):
    for obj in page.get("Contents", []):
        total_objects += 1
        total_size += obj["Size"]

        age = (
            datetime.now(timezone.utc) - obj["LastModified"]
        ).days

        print("\nObject:", obj["Key"])
        print("Size:", obj["Size"], "bytes")
        print("Age:", age, "days")

        if age > AGE_THRESHOLD_DAYS:
            print("Recommendation: Review for archival or deletion.")
        else:
            print("Status: Recently modified.")

print("\nTotal Objects:", total_objects)
print("Total Size:", round(total_size / (1024 * 1024), 4), "MB")
print("\nS3 analysis completed!")
