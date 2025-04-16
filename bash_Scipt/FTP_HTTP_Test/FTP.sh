#!/bin/bash

HOST="192.188.11.22"            # Replace with your FTP server's IP address or hostname
USER="anonymous"                # FTP username (anonymous in this case)
#PASSWORD=""                     # FTP password (empty in this case)
REMOTE_DIR="new"                # Remote directory on the FTP server
FILE="200MB"             # File to upload
#NUM_UPLOADS=5                   # Number of times to repeat the loop
SLEEP_TIME=10                    # Time in seconds to sleep between iterations
DURATION=$((60 * 5))     # Duration in seconds (7 days)
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
  echo "UPload file...Cycle"$counter
  echo "startTest: "$current_date>> $logfile
  # Connect to the FTP server and perform the necessary commands
  ftp -n $HOST <<END_SCRIPT
  quote USER $USER
  cd $REMOTE_DIR
  put $FILE
  delete $FILE
  quit
END_SCRIPT
  echo "File uploaded and deleted."
  echo "ENDTest: "$current_date>> $logfile
  echo "Cycle $counter completed." >> $logfile
  echo "=========">> $logfile
  echo "Next download in $SLEEP_TIME seconds..."
  sleep $SLEEP_TIME  # Add a sleep command to introduce a delay between iterations
  echo "Cycle $counter completed. Moving to the next iteration."
done
