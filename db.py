import sqlite3
DATABASE_NAME = "TAREA"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS Admin(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
				password TEXT NOT NULL
            )
            """,
        """CREATE TABLE IF NOT EXISTS Company(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company_name TEXT NOT NULL,
				company_api_key TEXT NOT NULL
            )
            """,
        """CREATE TABLE IF NOT EXISTS Location(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                company_id INTEGER,
                location_name TEXT NOT NULL,
				location_country TEXT NOT NULL,
                location_city TEXT NOT NULL,
                location_meta TEXT NOT NULL
            )
            """,
        """CREATE TABLE IF NOT EXISTS Sensor(
                sensor_id INTEGER PRIMARY KEY AUTOINCREMENT,
                location_id INTEGER,
                sensor_name TEXT NOT NULL,
                sensor_category TEXT NOT NULL,
                sensor_meta TEXT NOT NULL,
                sensor_api_key TEXT NOT NULL
            )
            """,
        """CREATE TABLE IF NOT EXISTS SensorData(
                sensor_id INTEGER,
                var1 TEXT NOT NULL,
                var2 TEXT NOT NULL,
                var3 TEXT NOT NULL,
				var4 TEXT NOT NULL
            )
            """   
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)
