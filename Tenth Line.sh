#!/bin/bash

# Initialize the counter (no spaces around =)
count=0

# A file to read from. Create one for testing.
# For example: seq 1 20 > file.txt
input_file="file.txt"

while IFS= read -r line; do

  # Use arithmetic expansion to increment the counter
  ((count++))

  # Check if the counter equals 10 using a numeric comparison
  if [[ $count -eq 10 ]]; then
    echo $line
  fi
  
  # This will still print every line from the file
  # echo "Line content: $line"

done < $input_file
