#!/bin/bash

echo "Running app..."
echo
python /eventgen/app/main.py \
    --sftp_host $SFTP_HOST \
    --sftp_user $SFTP_USER \
    --sftp_pass $SFTP_PASSWORD \
    --sftp_port $SFTP_PORT \
    --output_prefix $OUTPUT_PREFIX \
    --file_element $FILE_ELEMENT \
    --input_file "/eventgen/resources/data/$INPUT_FILE"

echo "Finished app!!"
