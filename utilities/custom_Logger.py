import logging
import os


class LogGen:
    @staticmethod
    def loggen():

        logger = logging.getLogger('selenium')
        file_handler = logging.FileHandler(os.path.abspath(os.curdir) + '\\logs\\automation.log')
        file_handler.setFormatter(logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p'))
        # logger.setLevel(logging.DEBUG)
        logger.setLevel(logging.INFO)
        logger.addHandler(file_handler)
        return logger

#
# # Configures the logger with a specific format for log messages:
# # %(asctime)s: Timestamp of the log message.
# # %(levelname)s: Log level (e.g., DEBUG, INFO, ERROR).
# # %(message)s: The actual log message.
# # datefmt='%m/%d/%Y %I:%M:%S %p': Specifies the date and time format.