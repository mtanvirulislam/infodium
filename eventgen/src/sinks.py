import csv
import time
from glob import glob
from os import path

import mysql.connector as con
import pandas as pd
from kafka.producer import KafkaProducer

from config.connector import *


def load_data_mysql(config):
    print("Start mysql data loader")

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

    print("Files load to MySql:")
    # Save data to MySql table
    for file in files:
        print("- {path}".format(path=file))
        table = path.splitext(path.basename(file))[0]
        pd.read_csv(file).to_sql(
            table, con=engine, if_exists='replace', index=False
        )


def send_event_kafka(config):
    print("Start event generator")

    total_events = 0

    # Read input CSV
    reader = csv.DictReader(
        open("{data_dir}/sftp/{file}".format(data_dir=config.data_dir, file=config.input_file), 'r')
    )

    producer = KafkaProducer(
        bootstrap_servers='{host}:{port}'.format(host=config.kafka_host, port=config.kafka_port),
        api_version=(0, 10, 1)
    )

    for row in reader:
        producer.send(config.kafka_topic, bytes(str(row), 'utf-8'))
        total_events += 1
        time.sleep(config.delay)

    print("Total Events: {total}".format(total=total_events))
