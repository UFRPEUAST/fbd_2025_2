import psycopg2
from app import config


class DataBaseConnect:
    @classmethod
    def get_connection(cls):
        conn = psycopg2.connect(config.DATABASE_URL)
        return conn
