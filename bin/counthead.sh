#!/bin/bash

# Check if filename is supplied
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 filename"
    exit 1
fi

# Store the filename argument in a variable
filename=$1

# Use awk to count fields
awk -F"," '{print NF; exit}' "$filename"

