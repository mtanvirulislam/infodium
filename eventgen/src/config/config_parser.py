import argparse


def get_config():
    # Instantiate the parser
    parser = argparse.ArgumentParser(description='App arguments parser')

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

    # KAFKA HOST
    parser.add_argument('--kafka_host', type=str)

    # KAFKA PORT
    parser.add_argument('--kafka_port', type=int)

    # KAFKA TOPIC
    parser.add_argument('--kafka_topic', type=str, default='football')

    # OUTPUT DELAY
    parser.add_argument('--delay', type=float, default=2)

    # INPUT FILE NAME
    parser.add_argument('--input_file', type=str)

    # DATA DIRECTORY
    parser.add_argument('--data_dir', type=str, default='/eventgen/resources/data')

    return parser.parse_args()

