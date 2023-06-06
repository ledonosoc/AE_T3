"""
    API REST con Python 3 y SQLite 3
    By Parzibyte: 
    ** https://parzibyte.me/blog **
"""

from flask import Flask, jsonify, request
import admin, location, sensor, sensor_data
from db import create_tables

app = Flask(__name__)

@app.route("/api/v1/company", methods=["POST"])
def insert_company():
    company_details = request.get_json()
    company_name = company_details["company_name"]
    company_api_key = company_details["company_api_key"]
    result = admin.insert_company(company_name, company_api_key)
    return jsonify(result)

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
    return jsonify(result)

@app.route("/api/v1/sensor", methods=["POST"])
def insert_sensor():
    sensor_details = request.get_json()
    location_id = sensor_details["location_id"]
    sensor_name = sensor_details["sensor_name"]
    sensor_category = sensor_details["sensor_category"]
    sensor_meta = sensor_details["sensor_meta"]
    sensor_api_key = sensor_details["sensor_api_key"]
    result = sensor.insert_sensor(location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key)
    return jsonify(result)

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
    return jsonify(result)


@app.route("/api/v1/company/<id>", methods=["GET"])
def get_company_by_id(id):
    company_details = request.get_json()
    company_api_key = company_details["company_api_key"]
    data_company = admin.get_by_id(id, company_api_key)
    return jsonify(data_company)

@app.route("/api/v1/location/<id>", methods=["GET"])
def get_location_by_id(id):
    location_details = request.get_json()
    company_api_key = location_details["company_api_key"]
    data_location = location.get_by_id(id, company_api_key)
    return jsonify(data_location)

@app.route("/api/v1/sensor/<id>", methods=["GET"])
def get_sensor_by_id(id):
    sensor_details = request.get_json()
    company_api_key = sensor_details["company_api_key"]
    data_sensor = sensor.get_by_id(id, company_api_key)
    return jsonify(data_sensor)

@app.route("/api/v1/sensor_data/<id>", methods=["GET"])
def get_sensor_data_by_id(id):
    sensor_data_details = request.get_json()
    sensor_api_key = sensor_data_details["sensor_api_key"]
    data_sensor_data = sensor_data.get_sensor_data(sensor_api_key)
    return jsonify(data_sensor_data)

@app.route('/api/v1/companies', methods=["GET"])
def get_companies():
    companies = admin.get_companies()
    return jsonify(companies)

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

@app.route("/api/v1/company", methods=["PUT"])
def update_company():
    company_details = request.get_json()
    company_id = company_details["company_id"]
    company_name = company_details["company_name"]
    new_company_api_key = company_details["new_company_api_key"]
    company_api_key = company_details["company_api_key"]
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
    result = sensor.update_sensor(sensor_id, location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key, company_api_key)
    return jsonify(result)

@app.route("/api/v1/sensor_data", methods=["PUT"])
def update_sensor_data():
    sensor_data_details = request.get_json()
    sensor_id = sensor_data_details["location_id"]
    var1 = sensor_data_details["company_id"]
    var2 = sensor_data_details["location_name"]
    var3 = sensor_data_details["location_country"]
    var4 = sensor_data_details["location_city"]
    sensor_api_key = sensor_data_details["company_api_key"]
    result = location.update_location(sensor_id, var1, var2, var3, var4, sensor_api_key)
    return jsonify(result)

@app.route("/api/v1/company/<id>", methods=["DELETE"])
def delete_company(id):
    company_details = request.get_json()
    company_api_key = company_details["company_api_key"]
    result = admin.delete_company(id,company_api_key)
    return jsonify(result)

@app.route("/api/v1/location/<id>", methods=["DELETE"])
def delete_location(id):
    location_details = request.get_json()
    company_api_key = location_details["company_api_key"]
    result = location.delete_location(id,company_api_key)
    return jsonify(result)

@app.route("/api/v1/sensor/<id>", methods=["DELETE"])
def delete_sensor(id):
    sensor_details = request.get_json()
    company_api_key = sensor_details["company_api_key"]
    result = sensor.delete_sensor(id,company_api_key)
    return jsonify(result)

@app.route("/api/v1/sensor_data/<id>", methods=["DELETE"])
def delete_sensor_data(id):
    sensor_data_details = request.get_json()
    sensor_api_key = sensor_data_details["sensor_api_key"]
    result = sensor_data.delete_sensor_data(id,sensor_api_key)
    return jsonify(result)


if __name__ == "__main__":
    create_tables()
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.run(host='0.0.0.0', port=8000, debug=False)
