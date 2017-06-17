# project/config.py

class BaseConfig:
    '''Base configurations'''
    DEBUG = False
    TESTING = False

class DevelopmentConfig(BaseConfig):
    '''Development configuration'''
    DEBUG = True

class TestingConfig(BaseConfig):
    '''Testing configuration'''
    DEBUG = True

class ProductionConfig(BaseConfig):
    '''prodction configration'''
    DEBUG = False
