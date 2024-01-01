#!/bin/bash

# Check if argument was supplied
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 filename"
    exit 1
fi

# Set filename argument
filename=$1

# Perform scp operation
scp -i flurine.pem ubuntu@ec2-16-171-47-69.eu-north-1.compute.amazonaws.com:/home/ubuntu/$filename ~/MA/data/dwnld

