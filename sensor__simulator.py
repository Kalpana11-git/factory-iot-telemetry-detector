import boto3
import json
import time
import random

# AWS connection setup (Step-1 la edutha Access Keys inga podanum)

AWS_REGION = "us-east-1"  

# Lambda client connect panrom
lambda_client = boto3.client(
    'lambda',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY,
    region_name=AWS_REGION
)

print("Heavy Machine IoT Sensor Simulation Started...")

# Oru machine-la irunthu continuous-ah data varra madhiri loop panrom
for i in range(5):
    # Random-ah temperature 40°C kku 95°C kku ulla varum
    fake_temp = random.randint(40, 95)
    
    payload = {
        "machine_id": "Caterpillar-Engine-909",
        "temperature": fake_temp
    }
    
    print(f"Sending telemetry -> Temperature: {fake_temp}°C")
    
    # AWS Lambda function-a laptop-la irunthu trigger panrom
    response = lambda_client.invoke(
        FunctionName='factory-anomaly-checker',
        InvocationType='Event',
        Payload=json.dumps(payload)
    )
    
    time.sleep(3) # 3 seconds gap vitu next reading anuppum

print("Simulation finished! Check your email for high temperature alerts.")