from app.connection.database import DataBaseConnect


class CourseRepository:
    def __init__(self):
        pass

    def get_all(self):
        query = "SELECT version();"
        conn = DataBaseConnect.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            return cursor.fetchall()
        finally:
            conn.close()
        return []

    def get(self, id, params=None):
        query = "SELECT version();"
        conn = DataBaseConnect.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchone()
        finally:
            conn.close()
        return None
