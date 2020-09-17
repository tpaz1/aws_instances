#aws_instances
this project will help you manage, monitor and track your up and running aws ec2 instances with ELK stack.

Our `python` script connects to our `aws` account using `boto3` and outputs the number of our up and running `ec2 instances` and their IP's.

Our `Dockerfile` builds our image locally using `Base image` alpine-awscli.

After our `docker` image is ready and we pushed it to our repository (`Docker hub`) we start with the `kubernetes` part. 
