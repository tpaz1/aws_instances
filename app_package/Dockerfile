FROM woahbase/alpine-awscli:latest
WORKDIR /usr/src/app
COPY ec2_instance.py .
EXPOSE 8080
CMD [ "python" , "ec2_instance.py" ]

