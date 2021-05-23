import csv
import time
from glob import glob
from os import path

import mysql.connector as con
import pandas as pd

from config.connector import *
from config.functions import *


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


def send_event_sftp(config):
    print("Start event generator")
    count = 0

    # Clear tmp dir
    tmp_dir = config.tmp_dir
    clear_tmp_sftp(tmp_dir)

    # Read input CSV
    reader = csv.DictReader(
        open("{data_dir}/sftp/{file}".format(data_dir=config.data_dir, file=config.input_file), 'r')
    )

    # Create Initial output file
    output_json = open(tmp_dir + get_output_file_name(config.output_prefix), 'w')

    # Connect with SFTP
    sftp = get_sftp(config)
    print("Connection succesfully stablished ... ")

    # In case of single_file_output convert the csv to a json file with all the records
    if config.single_file_output:
        for row in reader:
            # Write to local tmp directory
            row_writer(row, output_json)

        # Put file to SFTP and clear local tmp dir
        sftp_put(sftp, output_json, tmp_dir)

    # If not single_file_output the output depends on file_element(number of records that each file will contain)
    else:
        for row in reader:
            # Write to local tmp directory
            row_writer(row, output_json)
            count += 1

            if config.file_element == count:
                # Put previous file to SFTP and clear local tmp dir
                sftp_put(sftp, output_json, tmp_dir)

                # Set row count to 0 and wait 2sec(default)
                count = 0
                time.sleep(config.delay)

                # Create new file
                output_json = open(tmp_dir + get_output_file_name(config.output_prefix), 'w')

        # Put last file to SFTP and clear local tmp dir
        sftp_put(sftp, output_json, tmp_dir)

    sftp.close()
    print("Connection closed!!")
