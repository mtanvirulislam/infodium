import csv
import json
import time
from glob import glob
from os import path
from datetime import datetime

import mysql.connector as con
import pandas as pd
from kafka.producer import KafkaProducer

from config.connector import *
from config.utils import printlog


def load_data_mysql(config):
    printlog("Start mysql data loader")

    # Create initial connection
    connection = con.connect(
        host=config.mysql_host,
        user=config.mysql_user, password=config.mysql_pass
    )
    cursor = connection.cursor()

    # Create database
    cursor.execute(
        "CREATE DATABASE IF NOT EXISTS {database}".format(database=config.mysql_database)
    )

    # Create MySql engine
    engine = get_mysql_engine(config)

    # Get files to ingest
    files = glob("{data_dir}/mysql/**/*.csv".format(data_dir=config.data_dir), recursive=True)

    printlog("Files load to MySql:")
    # Save data to MySql table
    for file in files:
        print("\t{path}".format(path=file))
        table = path.splitext(path.basename(file))[0]
        pd.read_csv(file).to_sql(
            table, con=engine, if_exists='replace', index=False
        )


def send_event_kafka(config):
    printlog("Start event generator")

    total_events = 0

    printlog(
        "Files send to Kafka: \n {file}".format(
            file="\t{data_dir}/kafka/{file}".format(data_dir=config.data_dir, file=config.input_file)
        )
    )

    # Read input CSV
    reader = csv.DictReader(
        open("{data_dir}/kafka/{file}".format(data_dir=config.data_dir, file=config.input_file), 'r')
    )

    # Create kafka producer
    producer = KafkaProducer(
        bootstrap_servers='{host}:{port}'.format(host=config.kafka_host, port=config.kafka_port),
        api_version=(0, 10, 1),
        value_serializer=lambda v: json.dumps(v).encode('utf-8'),
        key_serializer=lambda v: json.dumps(v).encode('utf-8')
    )

    # Send data to kafka topic
    for row in reader:
        # Add event timestamp
        row["event_time"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        producer.send(config.kafka_topic, row)
        total_events += 1
        
        printlog(f"Event ID: {row.get('id_event')} - Event number: {total_events} - Event time: {row.get('event_time')}")
        time.sleep(config.delay)

    printlog("Total Events: {total}".format(total=total_events))
