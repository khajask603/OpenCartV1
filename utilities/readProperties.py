import configparser
import os

config_file_path = os.path.abspath(os.curdir) + r"\configurations\config.ini"
config = configparser.RawConfigParser()
config.read(config_file_path)


class ReadConfig:
    @staticmethod
    def getApplicationUrl():
        URL=config.get('commonInfo','baseurl')
        return URL

    @staticmethod
    def getEmail():
        email = config.get('commonInfo', 'email')
        return email

    @staticmethod
    def getPaswword():
        password = config.get('commonInfo', 'password')
        return password