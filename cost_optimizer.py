
import subprocess
import sys
from datetime import datetime

print("=" * 45)
print("AWS DEVOPS COST OPTIMIZER")
print("=" * 45)
print("Report generated:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

scripts = [
    "ec2_optimizer.py",
    "ebs_optimizer.py",
    "s3_optimizer.py"
]

for script in scripts:
    print(f"\nRunning {script}...")

    result = subprocess.run(
        [sys.executable, script],
        capture_output=True,
        text=True
    )

    print(result.stdout)

    if result.returncode != 0:
        print("ERROR:", result.stderr)
        print(f"{script} failed.")
        sys.exit(result.returncode)

print("=" * 45)
print("ALL OPTIMIZATION CHECKS COMPLETED")
print("=" * 45)
