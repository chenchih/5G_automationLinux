#!/bin/bash

#URL="http://192.188.11.22/500MB.zip"  # Replace with the URL of the file you want to download
URL="http://192.188.11.22/"  # Replace with the URL of the file you want to download
filename="500MB.zip"
#filename="5MB.zip"
OUTPUT_DIR="."        # Replace with the directory where you want to save the file

#DURATION=$((60 * 5))     # Duration 5Minute
DURATION=$((60 * 60 *24 *3))     # Duration in seconds (7 days)
WAIT_MIN=600                      # Minimum wait time between downloads (in seconds)
WAIT_MAX=1800                     # Maximum wait time between downloads (in seconds)
logfile="logtext.txt"
start_time=$(date +%s)
end_time=$((start_time + DURATION))
current_date=$(date)
counter=0
while [[ $(date +%s) -lt $end_time ]]
do
  counter=$((counter + 1))
  echo "Downloading file...Cycle"$counter
  
  echo "start Test: "$current_date>> $logfile
  wget "$URL$filename" -P "$OUTPUT_DIR"

  #sleep_time=$((WAIT_MIN + RANDOM % (WAIT_MAX - WAIT_MIN)))
  sleep_time=10
  echo "END Test: "$current_date>> $logfile
  echo "Cycle $counter completed." >> $logfile
  echo "==========">> $logfile
  rm $filename
  echo "Next download in $sleep_time seconds..."
  sleep "$sleep_time"
  echo "Cycle $counter completed. Moving to the next iteration."

done
