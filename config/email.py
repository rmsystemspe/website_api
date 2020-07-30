import os

mailers = {
    'mailers': {
        'smtp': {
            'server': os.getenv('MAIL_SERVER', 'smtp.mailtrap.io'),
            'port': os.getenv('MAIL_PORT', '2525'),
            'encryption': os.getenv('MAIL_ENCRYPTION', 'tls'),
            'username': os.getenv('MAIL_USERNAME'),
            'password': os.getenv('MAIL_PASSWORD'),
            'use_tls': os.getenv('MAIL_USE_TLS', True),
            'use_ssl': os.getenv('MAIL_USE_SSL', False)
        }
    }
}
