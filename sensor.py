from db import get_db


def insert_sensor(location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO sensor(location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(statement, [location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key])
    db.commit()
    return True


def update_sensor(id, location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE sensor SET location_id = ?, sensor_name = ?, sensor_category = ?, sensor_meta = ?, sensor_api_key = ? WHERE id = ?"
    cursor.execute(statement, [location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key, id])
    db.commit()
    return True


def delete_sensor(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM sensor WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key FROM sensor WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()


def get_sensors():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key FROM sensor"
    cursor.execute(query)
    return cursor.fetchall()
