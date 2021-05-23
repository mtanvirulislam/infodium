import mysql.connector as conn
import pysftp
from sqlalchemy import create_engine


def get_sftp(config):
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    return pysftp.Connection(
        host=config.sftp_host,
        username=config.sftp_user, password=config.sftp_pass, port=config.sftp_port,
        cnopts=cnopts
    )


def get_mysql(config):
    return conn.connect(
        host=config.mysql_host,
        user=config.mysql_user, password=config.mysql_pass
    )


def get_mysql_engine(config):
    return create_engine(
        "mysql+pymysql://{user}:{password}@{host}/{database}".format(
            host=config.mysql_host,
            user=config.mysql_user, password=config.mysql_pass,
            database=config.mysql_database
        )
    )
