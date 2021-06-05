import logging
import sys


def printlog(log):
    logging.basicConfig(level=logging.INFO,
                        format='[%(asctime)s] [%(levelname)s]: %(message)s',
                        handlers=[logging.StreamHandler(sys.stdout)])
    logging.info(log)