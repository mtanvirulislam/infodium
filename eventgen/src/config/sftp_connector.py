import pysftp


def get_sftp(config):
    cnopts = pysftp.CnOpts()
    cnopts.hostkeys = None
    return pysftp.Connection(
        host=config.sftp_host,
        username=config.sftp_user, password=config.sftp_pass, port=config.sftp_port,
        cnopts=cnopts
    )
