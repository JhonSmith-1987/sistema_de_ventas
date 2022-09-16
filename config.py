class Config:
    SECRET_KEY = 'lunaratoncomecarton'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'sistema_ventas'


config = {
    'development': DevelopmentConfig
}
