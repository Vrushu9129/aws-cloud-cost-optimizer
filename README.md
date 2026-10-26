# AWS DevOps Cost Optimizer

A Python-based, read-only AWS cost optimization proof of concept that analyzes EC2 CPU utilization, identifies unattached EBS volumes, and reviews S3 object storage.

## Project Overview

The goal of this project is to identify potential AWS resource inefficiencies using Python, boto3, and AWS monitoring APIs.

This is a learning project that generates recommendations without automatically stopping, modifying, or deleting AWS resources.

## Technologies Used

- **Cloud:** AWS EC2, CloudWatch, EBS, S3, IAM
- **Programming:** Python
- **AWS SDK:** boto3
- **Development:** VS Code, AWS CLI
- **Version Control:** Git and GitHub

## Architecture

AWS EC2 → CloudWatch CPU Metrics → Python Analysis

AWS EBS → Unattached Volume Detection → Python Analysis

AWS S3 → Object Age and Size Analysis → Python Analysis

All three checks → Combined Optimization Report

## Features

### 1. EC2 CPU Analysis
- Retrieves CPU utilization metrics from CloudWatch.
- Uses a custom 10% CPU threshold to flag potential underutilization.
- Generates recommendations for manual review.

### 2. EBS Volume Analysis
- Identifies EBS volumes in the `available` state.
- Flags unattached volumes for review.
- Does not delete any volumes.

### 3. S3 Storage Analysis
- Lists objects in a configured S3 bucket.
- Calculates object age and size.
- Flags objects older than 30 days for review.
- Does not modify or delete objects.

### 4. Combined Report
Runs all three Python scripts and displays their results in one terminal report.

## Project Files

```text
aws-devops-cost-optimizer/
├── main.py
├── ec2_optimizer.py
├── ebs_optimizer.py
├── s3_optimizer.py
├── cost_optimizer.py
├── requirements.txt
├── .gitignore
├── README.md
└── screenshots/
```

## How to Run

**Prerequisites:** Python 3, AWS CLI, and AWS credentials with the required read permissions.

1. Clone the repository.
2. Install dependencies:

```bash
python -m pip install -r requirements.txt
```

3. Configure AWS credentials securely using an IAM identity.
4. Update the region, EC2 Name tag, and S3 bucket name in the scripts as needed.
5. Run:

```bash
python cost_optimizer.py
```

## Sample Test Results

Tested on October 26, 2026:

| Resource | Result |
|---|---|
| EC2 | Stopped instance; average CPU 0.13% across five samples |
| EBS | No unattached volumes detected |
| S3 | One object, 15 bytes, recently modified |
| Overall | All three checks completed |

These results demonstrate API connectivity and rule-based analysis. They do not establish verified cost savings.

## Limitations

- CPU utilization is evaluated over a short monitoring window.
- CPU utilization alone is insufficient for a reliable rightsizing decision.
- S3 object age does not establish whether an object is unused.
- The scripts do not calculate actual monetary savings.
- Analysis is read-only and runs manually on a local computer.
- The EC2 and EBS checks use the configured AWS region.

## What I Learned

- How to access AWS services using Python and boto3.
- How to retrieve CloudWatch CPU utilization metrics.
- How to detect unattached EBS volumes.
- How to inspect S3 object metadata.
- How to authenticate using AWS IAM credentials.
- How to combine multiple automation scripts into a single report.

## Future Improvements

- Longer-term EC2 monitoring.
- More accurate cost estimates.
- CSV or JSON report generation.
- Optional Lambda scheduling and SNS notifications.
- More precise IAM permissions.

## Disclaimer

This is an educational proof of concept, not a production-ready cost optimization solution. Review all recommendations before making infrastructure changes.