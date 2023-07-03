#!/bin/bash

#python some2.py "$@"
output=$(python some2.py "$@")
IFS=';' read -r -a arrays <<< "$output"
echo "ok"
# Split each array using the delimiter (,)
IFS=',' read -r -a array1 <<< "${arrays[0]}"
IFS=',' read -r -a array2 <<< "${arrays[1]}"

while true; do
  clear
  echo "Select to play:"
  
  # Print the options
  for ((i = 0; i < ${#array1[@]}; i++)); do
    echo "$((i + 1)). ${array1[i]}"
  done
  
  read -p "Enter your choice (1-${#array1[@]}) or 'q' to quit: " choice
  
  if [[ $choice == "q" ]]; then
    break
  elif ((choice >= 1 && choice <= ${#array1[@]})); then
    index=$((choice - 1))
    command="/usr/bin/qbittorrent \"${array2[index]}\""
    eval "$command"
    echo "${array1[index]}"
    sleep 2  # Adjust the sleep duration as desired
  else
    echo "Invalid choice. Please try again."
    sleep 2  # Adjust the sleep duration as desired
  fi
done
