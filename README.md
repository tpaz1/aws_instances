#                                             **aws_instances**
##### this project will help you manage, monitor and track your up and running aws `ec2 instances` with `ELK stack`.
### Pre requirements

- Existing `Cluster` 
- `kubectl` [Installation](https://kubernetes.io/docs/tasks/tools/install-kubectl/)
- `Docker` [Installation](https://docs.docker.com/engine/install/)

Our [`python`](./app_package/ec2_instance.py) script connects to our `aws` account using `boto3` and outputs the number of our up and running `ec2 instances` and their IP's.

Our [`Dockerfile`](./app_package/Dockerfile) builds our image locally using `Base image` alpine-awscli.

After our `docker` image is ready and we pushed it to our repository (`Docker hub`) we start with the `kubernetes` part. 

In the `k8s` part we deploy our appliction which runs on port 8080 by pulling the Docker image we created from [Docker hub](https://hub.docker.com/?ref=login) 

## ECK Cluster

Our ECK Cluster setup built as followed:

- 2X Pods of `MASTER` + `DATA` (master + data will run together) 
- 2X Pods  of `Ingest Node`
- 2X Pods of `Coordinator` nodes

Our setup require the Master and Data node to have persistent storage,
Along with the minimal CPU + RAM request configured for the pods.

The coordinator role in this cluster is to forward the logs from our python appliction to the data node which holds the data.
Then, using `Kibana` we will create dashboards of our indexed data to view and visualize our up and running `ec2 instances` in a very nice and interactive way. 


