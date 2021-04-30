import csv
import time

from config.config_parser import *
from config.sftp_connector import *
from functions import *

if __name__ == '__main__':

    count = 0
    config = get_config()

    # Clear tmp dir
    tmp_dir = config.tmp_dir
    clear_tmp_sftp(tmp_dir)

    # Read input CSV
    reader = csv.DictReader(open(config.input_file, 'r'))

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
