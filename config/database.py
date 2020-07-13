import os


database = {
        'connections': {
            'mysql': {
                'driver': 'mysql',
                'host': os.getenv('DB_HOST', '127.0.0.1'),
                'port': os.getenv('DB_PORT', '3306'),
                'database': os.getenv('DB_DATABASE', 'flask'),
                'username': os.getenv('DB_USERNAME', 'root'),
                'password': os.getenv('DB_PASSWORD')
            },

            'pgsql': {
                'driver': 'pgsql',
                'host': os.getenv('DB_HOST', '127.0.0.1'),
                'port': os.getenv('DB_PORT', '5432'),
                'database': os.getenv('DB_DATABASE', 'flask'),
                'username': os.getenv('DB_USERNAME', 'root'),
                'password': os.getenv('DB_PASSWORD')
            }
        }
    }


def create_database_url():
    conn = os.getenv('DB_CONNECTION', 'mysql')
    db_conf = database['connections'][conn]

    return f'{db_conf["driver"]}://{db_conf["username"]}:{db_conf["password"]}@{db_conf["host"]}/{db_conf["database"]}'