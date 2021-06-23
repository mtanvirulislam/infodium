import mysql.connector as conn
from sqlalchemy import create_engine


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
