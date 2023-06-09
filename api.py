"""
    Código adaptado de 
    API REST con Python 3 y SQLite 3
    By Parzibyte
    https://parzibyte.me/blog/2020/11/10/api-rest-python-flask-sqlite3/
"""

from flask import Flask, jsonify, request, Response
import admin, location, sensor, sensor_data, secrets
from db import create_tables

app = Flask(__name__)

@app.route("/api/v1/company", methods=["POST"])
def insert_company():
    company_details = request.get_json()
    company_name = company_details["company_name"]
    company_api_key = secrets.token_hex(20)
    result = admin.insert_company(company_name, company_api_key)
    if result == True:
        return Response( "{\"Created succesfully\",{\"company_api_key\"="+company_api_key+"}}" , status=201, mimetype="application/json")
    else:
        return 400


@app.route("/api/v1/location", methods=["POST"])
def insert_location():
    location_details = request.get_json()
    company_id = location_details["company_id"]
    location_name = location_details["location_name"]
    location_country = location_details["location_country"]
    location_city = location_details["location_city"]
    location_meta = location_details["location_meta"]
    company_api_key = location_details["company_api_key"]
    result = location.insert_location(company_id, location_name, location_country, location_city, location_meta, company_api_key)
    if result == True:
        return "CREATED", 201
    else:
        return "",400


@app.route("/api/v1/sensor", methods=["POST"])
def insert_sensor():
    sensor_details = request.get_json()
    location_id = sensor_details["location_id"]
    sensor_name = sensor_details["sensor_name"]
    sensor_category = sensor_details["sensor_category"]
    sensor_meta = sensor_details["sensor_meta"]
    sensor_api_key = secrets.token_hex(40)
    result = sensor.insert_sensor(location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key)
    if result == True:
        return "CREATED", 201
    else:
        return 400

@app.route("/api/v1/sensor_data", methods=["POST"])
def insert_sensor_data():
    sensor_data_details = request.get_json()
    sensor_id = sensor_data_details["sensor_id"]
    var1 = sensor_data_details["var1"]
    var2 = sensor_data_details["var2"]
    var3 = sensor_data_details["var3"]
    var4 = sensor_data_details["var4"]
    sensor_api_key = sensor_data_details["sensor_api_key"]
    result = sensor.insert_sensor(sensor_id, var1, var2, var3, var4, sensor_api_key)
    if result == True:
        return "CREATED", 201
    else:
        return 400

@app.route("/api/v1/company/<id>", methods=["GET"])
def get_company_by_id(id):
    company_details = request.get_json()
    company_api_key = company_details["company_api_key"]
    data_company = admin.get_by_id(id)
    if data_company[2] == company_api_key:
        return str(data_company), 200
    else:
        return 400

@app.route("/api/v1/location/<id>", methods=["GET"])
def get_location_by_id(id):
    location_details = request.get_json()
    company_api_key = location_details["company_api_key"]
    data_location = location.get_by_id(id, company_api_key)
    data_company = admin.get_by_id(data_location[1])
    if data_company[2] == company_api_key:
        return str(data_location), 200
    else:
        return 400

@app.route("/api/v1/sensor/<id>", methods=["GET"])
def get_sensor_by_id(id):
    sensor_details = request.get_json()
    company_api_key = sensor_details["company_api_key"]
    data_sensor = sensor.get_by_id(id, company_api_key)
    data_location = location.get_by_id(data_sensor[1], company_api_key)
    data_company = admin.get_by_id(data_location[1])
    if data_company[2] == company_api_key:
        return str(data_sensor), 200
    else:
        return 400
    
@app.route("/api/v1/sensor_data/<id>", methods=["GET"])
def get_sensor_data_by_id(id):
    company_api_key = request.args.get("company_api_key")
    desde = request.args.get("desde")
    hasta = request.args.get("hasta")
    sensor_data_details = request.get_json()
    sensor_api_key = sensor_data_details["sensor_api_key"]
    data_sensor_data = sensor_data.get_sensor_data(sensor_api_key, desde, hasta)
    data_sensor = sensor.get_by_id(id, company_api_key)
    data_location = location.get_by_id(data_sensor[1], company_api_key)
    data_company = admin.get_by_id(data_location[1])
    if data_company[2] == company_api_key:
        return str(data_sensor_data), 200
    else:
        return 400
    
    
@app.route('/api/v1/companies', methods=["GET"])
def get_companies():
    companies = admin.get_companies()
    return str(companies), 200

@app.route('/api/v1/locations', methods=["GET"])
def get_locations():
    company_details = request.get_json()
    company_api_key = company_details["company_api_key"]
    locations = location.get_locations(company_api_key)
    return jsonify(locations)

@app.route('/api/v1/sensors', methods=["GET"])
def get_sensors():
    company_details = request.get_json()
    company_api_key = company_details["company_api_key"]
    sensors = sensor.get_sensors(company_api_key)
    return jsonify(sensors)

@app.route("/api/v1/sensors_data/", methods=["GET"])
def get_sensors_data_by_ids():
    company_api_key = request.args.get("company_api_key")
    desde = request.args.get("desde")
    hasta = request.args.get("hasta")
    sensores = request.args.get("ids")
    result = []
    for sensor_id in sensores:
        sensor_api_key = sensor.get_by_sensor(sensor_id)
        data_sensor_data = sensor_data.get_sensor_data(sensor_api_key, desde, hasta)
        result.append(data_sensor_data)
        data_sensor = sensor.get_by_id(data_sensor_data[0], company_api_key)
        data_location = location.get_by_id(data_sensor[1], company_api_key)
        data_company = admin.get_by_id(data_location[1])
        if data_company[2] != company_api_key:
            return "", 400
    return str(result), 200
            

@app.route("/api/v1/company", methods=["PUT"])
def update_company():
    company_details = request.get_json()
    company_id = company_details["company_id"]
    company_name = company_details["company_name"]
    new_company_api_key = company_details["new_company_api_key"]
    company_api_key = company_details["company_api_key"]
    data_company = admin.get_by_id(company_id)
    if data_company[2] != company_api_key:
        result = admin.update_company(company_id, company_name, new_company_api_key,company_api_key)
        return jsonify(result)

@app.route("/api/v1/location", methods=["PUT"])
def update_location():
    location_details = request.get_json()
    location_id = location_details["location_id"]
    company_id = location_details["company_id"]
    location_name = location_details["location_name"]
    location_country = location_details["location_country"]
    location_city = location_details["location_city"]
    location_meta = location_details["location_meta"]
    company_api_key = location_details["company_api_key"]
    data_company = admin.get_by_id(company_id)
    if data_company[2] != company_api_key:
        result = location.update_location(location_id, company_id, location_name, location_country, location_city , location_meta , company_api_key)
        return jsonify(result)

@app.route("/api/v1/sensor", methods=["PUT"])
def update_sensor():
    sensor_details = request.get_json()
    sensor_id = sensor_details["sensor_id"]
    location_id = sensor_details["location_id"]
    sensor_name = sensor_details["sensor_name"]
    sensor_category = sensor_details["sensor_category"]
    sensor_meta = sensor_details["sensor_meta"]
    sensor_api_key = sensor_details["sensor_api_key"]
    company_api_key = sensor_details["company_api_key"]
    data_sensor = sensor.get_by_id(sensor_id, company_api_key)
    data_location = location.get_by_id(data_sensor[1], company_api_key)
    data_company = admin.get_by_id(data_location[1])
    if data_company[2] != company_api_key:
        result = sensor.update_sensor(sensor_id, location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key, company_api_key)
        return jsonify(result)

@app.route("/api/v1/sensor_data", methods=["PUT"])
def update_sensor_data():
    sensor_data_details = request.get_json()
    sensor_id = sensor_data_details["sensor_id"]
    var1 = sensor_data_details["var_1"]
    var2 = sensor_data_details["var2"]
    var3 = sensor_data_details["var3"]
    var4 = sensor_data_details["var4"]
    password = sensor_data_details["sensor_api_key"]
    sensor_api_key = sensor.get_by_sensor(sensor_id)
    if password == sensor_api_key[1]:
        result = location.update_location(sensor_id, var1, var2, var3, var4, sensor_api_key)
        return jsonify(result)

@app.route("/api/v1/company/<id>", methods=["DELETE"])
def delete_company(id):
    company_details = request.get_json()
    company_api_key = company_details["company_api_key"]
    data = admin.get_by_id(id)
    if data[2] == company_api_key:
        result = admin.delete_company(id,company_api_key)
        if result == True:
            return "DELETED", 200

@app.route("/api/v1/location/<id>", methods=["DELETE"])
def delete_location(id):
    location_details = request.get_json()
    company_api_key = location_details["company_api_key"]
    location_data = location.get_by_id(id,company_api_key)
    company_data = admin.get_by_id(location_data[1])
    if company_data[2] == company_api_key:
        result = location.delete_location(id,company_api_key)
        if result == True:
            return "DELETED", 200


@app.route("/api/v1/sensor/<id>", methods=["DELETE"])
def delete_sensor(id):
    sensor_details = request.get_json()
    company_api_key = sensor_details["company_api_key"]
    data_sensor =  sensor.get_by_sensor(id)
    location_data = location.get_by_id(data_sensor[1], company_api_key)
    company_data = admin.get_by_id(location_data[1])
    if company_data[2] == company_api_key:
        result = sensor.delete_sensor(id,company_api_key)
        if result == True:
            return "DELETED", 200


@app.route("/api/v1/sensor_data/<id>", methods=["DELETE"])
def delete_sensor_data(id):
    sensor_data_details = request.get_json()
    sensor_api_key = sensor_data_details["sensor_api_key"]
    data_sensor = sensor.get_by_sensor(id)
    if data_sensor[1]==sensor_api_key:
        result = sensor_data.delete_sensor_data(id,sensor_api_key)
        if result == True:
                return "DELETED", 200



if __name__ == "__main__":
    create_tables()
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.run(host='0.0.0.0', port=8000, debug=True)
