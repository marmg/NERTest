# -*- coding: utf-8 -*-
from __future__ import absolute_import

import logging

logger = logging.getLogger()


def init_logger(log_file: str =None, log_file_level: int = logging.NOTSET):
    """ Init logger

    Keyword Arguments:
        :param log_file: (str) File to log in. If None, only will log to console
        :param log_file_level: (int) Level to log
    """
    logging.disable(logging.WARNING)
    log_format = logging.Formatter("[%(asctime)s %(levelname)s] %(message)s")
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    logger.handlers = [console_handler]

    if log_file and log_file != '':
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_file_level)
        file_handler.setFormatter(log_format)
        logger.addHandler(file_handler)

    return logger
