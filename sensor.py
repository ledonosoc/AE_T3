from db import get_db
import location, admin


def insert_sensor(location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key, company_api_key):
    data = location.get_by_id(location_id,company_api_key)
    company = admin.get_by_id(data[1])
    if(company[2] == company_api_key):
        db = get_db()
        cursor = db.cursor()
        statement = "INSERT INTO Sensor(location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(statement, [location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key])
        db.commit()
        return True
    else: 
        return False


def update_sensor(id, location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key, company_api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "WITH Company(id,company_api_key), Location(id,company_id), Sensor(id,location_id), UPDATE Sensor SET Sensor.location_id = ?, Sensor.sensor_name = ?, Sensor.sensor_category = ?, Sensor.sensor_meta = ?, Sensor.sensor_api_key = ? WHERE Sensor.id = ? AND Sensor.location_id = Location.id AND Location.company_id = Company.id AND Company.company_api_key = ?"
    cursor.execute(statement, [location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key, id, company_api_key])
    db.commit()
    return True


def delete_sensor(id, company_api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "WITH Company(id,company_api_key), Location(id,company_id), Sensor(id,location_id) DELETE FROM Sensor WHERE Sensor.id = ? AND Sensor.location_id = Location.id AND Location.company_id = Company.id AND Company.company_api_key = ?"
    cursor.execute(statement, [id, company_api_key])
    db.commit()
    return True


def get_by_id(id, company_api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "WITH Company(id,company_api_key), Location(id,company_id), Sensor(id,location_id) SELECT Sensor.id, Sensor.location_id, Sensor.sensor_name, Sensor.sensor_category, Sensor.sensor_meta, Sensor.sensor_api_key FROM Sensor WHERE Sensor.id = ? AND Sensor.location_id = Location.id AND Location.company_id = Company.id AND Company.company_api_key = ?"
    cursor.execute(statement, [id, company_api_key])
    return cursor.fetchone()

def get_by_sensor(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT Sensor.id,, Sensor.sensor_api_key FROM Sensor WHERE Sensor.id = ? "
    cursor.execute(statement, [id])
    return cursor.fetchone()

def get_sensors(company_api_key):
    db = get_db()
    cursor = db.cursor()
    query = "WITH Company(id,company_api_key), Location(id,company_id), Sensor(id,location_id) SELECT Sensor.id, Sensor.location_id, Sensor.sensor_name, Sensor.sensor_category, Sensor.sensor_meta, Sensor.sensor_api_key FROM Sensor WHERE Sensor.location_id = Location.id AND Location.company_id = Company.id AND Company.company_api_key = ? "
    cursor.execute(query, [company_api_key])
    return cursor.fetchall()
