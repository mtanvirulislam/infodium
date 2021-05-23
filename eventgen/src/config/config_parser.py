import argparse


def get_config():
    # Instantiate the parser
    parser = argparse.ArgumentParser(description='App arguments parser')

    # SFTP HOST
    parser.add_argument('--sftp_host', type=str)

    # SFTP USER
    parser.add_argument('--sftp_user', type=str)

    # SFTP PASSWORD
    parser.add_argument('--sftp_pass', type=str)

    # SFTP PORT
    parser.add_argument('--sftp_port', type=int, default=22)

    # MYSQL HOST
    parser.add_argument('--mysql_host', type=str)

    # MYSQL PORT
    parser.add_argument('--mysql_port', type=int, default=3306)

    # MYSQL USER
    parser.add_argument('--mysql_user', type=str, default='root')

    # MYSQL PASSWORD
    parser.add_argument('--mysql_pass', type=str)

    # MYSQL DATABASE
    parser.add_argument('--mysql_database', type=str, default='football')

    # OUTPUT EACH FILE ELEMENT
    parser.add_argument('--file_element', type=int, default=100)

    # OUTPUT DELAY
    parser.add_argument('--delay', type=int, default=10)

    # SFTP PASSWORD
    parser.add_argument('--input_file', type=str)

    # OUTPUT PREFIX
    parser.add_argument('--output_prefix', type=str)

    # DATA DIRECTORY
    parser.add_argument('--data_dir', type=str, default='/eventgen/resources/data')

    # TMP DIRECTORY
    parser.add_argument('--tmp_dir', type=str, default='/tmp/sftp_cache/')

    # OUTPUT FILE TYPE
    parser.add_argument('--single_file_output', action='store_true')

    return parser.parse_args()

