import boto3
import os

access_key = os.environ.get("AWS_ACCESS_KEY_ID")
secret_key = os.environ.get("AWS_SECRET_ACCESS_KEY")
session=boto3.Session(aws_access_key_id=access_key, aws_secret_access_key=secret_key, region_name="eu-west-1")
ec2=session.resource('ec2')
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])
count=0
for instance in instances: 
    print(instance.public_ip_address)
    count+=1 
print("number of running instances: " + str(count))
