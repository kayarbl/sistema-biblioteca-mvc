import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


class ConexaoDB:
    def __init__(self):
        self.config = {
            "host": os.getenv("DB_HOST"),
            "dbname": os.getenv("DB_NAME"),
            "user": os.getenv("DB_USER"),
            "password": os.getenv("DB_PASSWORD"),
            "port": os.getenv("DB_PORT"),
        }

    def conectar(self):
        try:
            return psycopg2.connect(**self.config)
        except Exception as erro:
            print("Erro ao conectar ao banco:", erro)
            return None