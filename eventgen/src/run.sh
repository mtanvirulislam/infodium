#!/bin/bash

echo "Running app..."
echo
python /eventgen/app/main.py \
    --mysql_host        $MYSQL_HOST \
    --mysql_user        $MYSQL_USER \
    --mysql_pass        $MYSQL_PASS \
    --mysql_database    $MYSQL_DATABASE \
    --kafka_host        $KAFKA_HOST \
    --kafka_port        $KAFKA_PORT \
    --kafka_topic       $KAFKA_TOPIC \
    --data_dir          $DATA_DIR \
    --input_file        $INPUT_FILE \
    --delay             $DELAY \
    | cat

echo "Finished app!!"
