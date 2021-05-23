import json
import os
import shutil
from datetime import datetime


def get_output_file_name(file_prefix):
    date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    return "{prefix}_{suffix}.json".format(prefix=file_prefix, suffix=date_time)


def row_writer(row, output_json_file):
    json.dump(row, output_json_file)
    output_json_file.write('\n')


def clear_tmp_sftp(path):
    shutil.rmtree(path)
    os.mkdir(path)


def sftp_put(sftp, output_json, tmp_dir):
    output_json.close()
    sftp.put(output_json.name)
    clear_tmp_sftp(tmp_dir)
