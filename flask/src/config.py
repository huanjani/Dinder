import os

class Development(object):
    """
    Development environment configuration
    """
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "postgresql://dinderpostgres:password@database-1.cvbo289m1v6g.us-west-2.rds.amazonaws.com:5432/postgres"#os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class Production(object):
    """
    Production environment configurations
    """
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = "postgresql://dinderpostgres:password@database-1.cvbo289m1v6g.us-west-2.rds.amazonaws.com:5432/postgres"#os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

app_config = {
    'development': Development,
    'production': Production,
}
