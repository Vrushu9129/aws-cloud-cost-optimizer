
import boto3
from datetime import datetime, timedelta, timezone

REGION = "ap-south-1"
CPU_THRESHOLD = 10

ec2 = boto3.client("ec2", region_name=REGION)
cloudwatch = boto3.client("cloudwatch", region_name=REGION)

end_time = datetime.now(timezone.utc)
start_time = end_time - timedelta(hours=3)

print("\nAWS EC2 COST OPTIMIZATION REPORT")
print("--------------------------------")

response = ec2.describe_instances(
    Filters=[
        {"Name": "tag:Name", "Values": ["cost optimiser"]}
    ]
)

found = False

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        found = True
        instance_id = instance["InstanceId"]
        state = instance["State"]["Name"]

        print(f"\nInstance: {instance_id}")
        print(f"State: {state}")

        metrics = cloudwatch.get_metric_statistics(
            Namespace="AWS/EC2",
            MetricName="CPUUtilization",
            Dimensions=[
                {"Name": "InstanceId", "Value": instance_id}
            ],
            StartTime=start_time,
            EndTime=end_time,
            Period=300,
            Statistics=["Average"]
        )

        datapoints = metrics.get("Datapoints", [])

        if not datapoints:
            print("No CPU metrics found in the last 3 hours.")
            print("Recommendation: Collect more monitoring data.")
            continue

        average_cpu = sum(
            point["Average"] for point in datapoints
        ) / len(datapoints)

        print(f"Average CPU: {average_cpu:.2f}%")
        print(f"Metric samples: {len(datapoints)}")

        if average_cpu < CPU_THRESHOLD:
            print("Status: Potentially underutilized")
            print("Recommendation: Review workload and rightsizing.")
        else:
            print("Status: No low-CPU flag")
            print("Recommendation: Continue monitoring.")

if not found:
    print("No EC2 instance found with the specified Name tag.")
