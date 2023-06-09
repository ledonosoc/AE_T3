from db import get_db
import sensor
import time

def insert_sensor_data(sensor_id, var1, var2, var3, var4, sensor_api_key):
    data = sensor.get_by_sensor(sensor_id)
    if(data["sensor_api_key"] == sensor_api_key):
        db = get_db()
        cursor = db.cursor()
        tiempo = time.time()
        statement = "INSERT INTO Sensor_data(sensor_id, tiempo, var1, var2, var3, var4) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(statement, [sensor_id, tiempo, var1, var2, var3, var4])
        db.commit()
        return True
    else: 
        return False


def update_sensor_data(sensor_id, var1, var2, var3, var4, sensor_api_key):
    db = get_db()
    cursor = db.cursor()
    tiempo = time.time()
    statement = "WITH Sensor(id,sensor_api_key), Sensor_data(sensor_id), UPDATE Sensor_data SET Sensor_data.time = ? , Sensor_data.var1 = ?, Sensor_data.var2 = ?, Sensor_data.var3 = ?, Sensor_data.var4 = ? WHERE Sensor_data.sensor_id = ? AND Sensor_data.sensor_id = Sensor.id AND Sensor.sensor_api_key = ?"
    cursor.execute(statement, [tiempo, var1, var2, var3, var4, sensor_id, sensor_api_key])
    db.commit()
    return True


def delete_sensor_data(sensor_id, sensor_api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "WITH Sensor(id,sensor_api_key), Sensor_data(sensor_id) DELETE FROM Sensor_data WHERE Sensor_data.sensor_id = ? AND Sensor_data.sensor_id = Sensor.id AND Sensor.sensor_api_key = ?"
    cursor.execute(statement, [sensor_id, sensor_api_key])
    db.commit()
    return True

def get_sensor_data(sensor_api_key, desde , hasta):
    db = get_db()
    cursor = db.cursor()
    query = "WITH Sensor(id,sensor_api_key), Sensor_data(id,company_id) SELECT Sensor.sensor_id, Sensor_data.time, Sensor_data.var1, Sensor_data.var2, Sensor_data.var3, Sensor_data.var4 FROM Sensor_data WHERE Sensor_data.sensor_id = Sensor.id AND Sensor.sensor_api_key = ? AND Sensor.time > ? AND Sensor.time < ? "
    cursor.execute(query, [sensor_api_key, desde, hasta])
    return cursor.fetchall()
