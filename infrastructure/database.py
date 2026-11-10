
import mysql.connector
from mysql.connector import Error


class Database:
    def __init__(
        self,
        host="127.0.0.1",
        user="root",
        password="",
        database="db_kampus",
        port=3306
    ):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port

    def get_connection(self):
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database,
                port=self.port
            )

            return connection

        except Error as e:
            raise RuntimeError(
                f"Gagal menghubungkan database Laragon: {e}"
            ) from e
