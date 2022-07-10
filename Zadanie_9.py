import logging


# logging.basicConfig(filename='log.txt', level=logging.DEBUG)
# logging.debug('To jest wiadomosc debugowa')
# logging.warning('To jest warning')

logging.basicConfig(level=logging.DEBUG)
logging.debug('To jest wiadomosc debugowa')
logging.warning('To jest warning')


class Formatter:

    @staticmethod
    def debug_log(text):
        logging.debug(f'\33[34m {text}')

    @staticmethod
    def warning_log(text):
        logging.warning(f'\33[34m {text}')

    @staticmethod
    def info_log(text):
        logging.info(f'\33[34m {text}')

    @staticmethod
    def critical_log(text):
        logging.critical(f'\33[91m{text}')


Formatter.debug_log('debug')
Formatter.warning_log('warning')
Formatter.info_log('info')
Formatter.critical_log('critical')


