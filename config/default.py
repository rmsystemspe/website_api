import os
from . import DATABASE_URI
from .email import mailers

mailer = mailers['mailers'][os.getenv('MAIL_DRIVER')]

SECRET_KEY = os.getenv('SECRET_KEY', os.urandom(64).hex())

PROPAGATE_EXCEPTIONS = True

# Database configuration
SQLALCHEMY_DATABASE_URI = DATABASE_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
SHOW_SQLALCHEMY_LOG_MESSAGES = False

# Email configuration
MAIL_SERVER = mailer['server']
MAIL_PORT = mailer['port']
MAIL_USERNAME = mailer['username']
MAIL_PASSWORD = mailer['password']
MAIL_USE_TLS = mailer['use_tls']

ERROR_404_HELP = False
