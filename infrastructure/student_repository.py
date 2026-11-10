
from domain.entities import Mahasiswa


class StudentRepository:
    def __init__(self, db):
        self.db = db

    def get_all(self):
        conn = self.db.get_connection()

        try:
            cursor = conn.cursor()

            query = """
                SELECT nim, nama, prodi, angkatan
                FROM mahasiswa
                ORDER BY nim
            """

            cursor.execute(query)
            rows = cursor.fetchall()

            return [
                Mahasiswa(
                    nim=row[0],
                    nama=row[1],
                    prodi=row[2],
                    angkatan=row[3]
                )
                for row in rows
            ]

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def add(self, mhs):
        conn = self.db.get_connection()

        try:
            cursor = conn.cursor()

            query = """
                INSERT INTO mahasiswa
                (nim, nama, prodi, angkatan)
                VALUES (%s, %s, %s, %s)
            """

            cursor.execute(
                query,
                (
                    mhs.nim,
                    mhs.nama,
                    mhs.prodi,
                    mhs.angkatan
                )
            )

            conn.commit()
            return cursor.rowcount > 0

        except Exception:
            conn.rollback()
            raise

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def update(self, mhs):
        conn = self.db.get_connection()

        try:
            cursor = conn.cursor()

            query = """
                UPDATE mahasiswa
                SET nama=%s, prodi=%s, angkatan=%s
                WHERE nim=%s
            """

            cursor.execute(
                query,
                (
                    mhs.nama,
                    mhs.prodi,
                    mhs.angkatan,
                    mhs.nim
                )
            )

            conn.commit()
            return cursor.rowcount > 0

        except Exception:
            conn.rollback()
            raise

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def delete(self, nim):
        conn = self.db.get_connection()

        try:
            cursor = conn.cursor()

            query = """
                DELETE FROM mahasiswa
                WHERE nim=%s
            """

            cursor.execute(query, (nim,))
            conn.commit()

            return cursor.rowcount > 0

        except Exception:
            conn.rollback()
            raise

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()

    def get_by_nim(self, nim):
        conn = self.db.get_connection()

        try:
            cursor = conn.cursor()

            query = """
                SELECT nim, nama, prodi, angkatan
                FROM mahasiswa
                WHERE nim=%s
            """

            cursor.execute(query, (nim,))
            row = cursor.fetchone()

            if row is None:
                return None

            return Mahasiswa(
                nim=row[0],
                nama=row[1],
                prodi=row[2],
                angkatan=row[3]
            )

        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
