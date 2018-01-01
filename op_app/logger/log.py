# coding:utf-8
import os
import logging
import logging.config as log_conf

log_dir = os.path.dirname(os.path.dirname(__file__)) + '/logs'
if not os.path.exists(log_dir):
    os.mkdir(log_dir)

log_path = os.path.join(log_dir, 'run.log')

log_config = {
    'version': 1.0,
    'formatters': {
        'detail': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S"
        },
        'simple': {
            'format': '%(name)s - %(levelname)s - %(message)s',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'INFO',
            'formatter': 'detail'
        },
        'file': {
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 1024 * 1024 * 5,
            'backupCount': 10,
            'filename': log_path,
            'level': 'INFO',
            'formatter': 'detail',
            'encoding': 'utf-8',
        },
    },
    'loggers': {
        'runlog': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
        'dblog': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
        },
    }
}

log_conf.dictConfig(log_config)

runlog = logging.getLogger('runlog')
dblog = logging.getLogger('dblog')


__all__ = ['runlog', 'dblog']


