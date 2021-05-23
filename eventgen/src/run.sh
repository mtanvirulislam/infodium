#!/bin/bash

echo "Running app..."
echo
python /eventgen/app/main.py \
    --mysql_host        $MYSQL_HOST \
    --mysql_user        $MYSQL_USER \
    --mysql_pass        $MYSQL_PASS \
    --mysql_database    $MYSQL_DATABASE \
    --sftp_host         $SFTP_HOST \
    --sftp_user         $SFTP_USER \
    --sftp_pass         $SFTP_PASSWORD \
    --sftp_port         $SFTP_PORT \
    --output_prefix     $OUTPUT_PREFIX \
    --file_element      $FILE_ELEMENT \
    --data_dir          $DATA_DIR \
    --input_file        $INPUT_FILE \
    --delay             $DELAY \
    | cat

echo "Finished app!!"
