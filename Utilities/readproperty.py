import configparser

config = configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")


class ReadConfig:

    @staticmethod
    def getURL():
        url = config.get('common-info', 'baseUrl')
        return url

    @staticmethod
    def getURL1():
        url = config.get('common-info', 'baseUrl2')
        return url

    @staticmethod
    def getUserName():
        username = config.get('common-info', 'userName')
        return username

    @staticmethod
    def getPassword():
        pw = config.get('common-info', 'password')
        return pw
