"""
    API REST con Python 3 y SQLite 3
    By Parzibyte: 
    ** https://parzibyte.me/blog **
"""
from flask import Flask, jsonify, request
import admin, location, sensor
from db import create_tables

app = Flask(__name__)

@app.route("api/v1/company", methods=["POST"])
def insert_company():
    company_details = request.get_json()
    company_name = company_details["company_name"]
    company_api_key = company_details["company_api_key"]
    result = admin.insert_company(company_name, company_api_key)
    return jsonify(result)

@app.route("api/v1/company/<id>", methods=["GET"])
def get_company_by_id(id):
    company_details = request.get_json()
    company_api_key = company_details["company_api_key"]
    data_company = admin.get_by_id(id, company_api_key)
    return jsonify(data_company)

@app.route("api/v1/location/<id>", methods=["GET"])
def get_location_by_id(id):
    location_details = request.get_json()
    company_api_key = location_details["company_api_key"]
    data_location = location.get_by_id(id, company_api_key)
    return jsonify(data_location)

@app.route("api/v1/sensor/<id>", methods=["GET"])
def get_company_by_id(id):
    sensor_details = request.get_json()
    company_api_key = sensor_details["company_api_key"]
    data_sensor = sensor.get_by_id(id, company_api_key)
    return jsonify(data_sensor)

@app.route("api/v1/sensor_data/<id>", methods=["GET"])
def get_company_by_id(id):
    sensor_data_details = request.get_json()
    sensor_api_key = sensor_data_details["sensor_api_key"]
    data_sensor_data = admin.get_by_id(id, sensor_api_key)
    return jsonify(data_sensor_data)

@app.route('api/v1/companies', methods=["GET"])
def get_companies():
    companies = admin.get_companies()
    return jsonify(companies)

@app.route('api/v1/locations', methods=["GET"])
def get_locations():
    company_details = request.get_json()
    company_api_key = company_details["company_api_key"]
    locations = location.get_locations(company_api_key)
    return jsonify(locations)

@app.route('api/v1/sensors', methods=["GET"])
def get_sensors():
    company_details = request.get_json()
    company_api_key = company_details["company_api_key"]
    sensors = sensor.get_sensors(company_api_key)
    return jsonify(sensors)

@app.route("api/v1/location", methods=["POST"])
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

@app.route("api/v1/sensor", methods=["POST"])
def insert_sensor():
    sensor_details = request.get_json()
    location_id = sensor_details["location_id"]
    sensor_name = sensor_details["sensor_name"]
    sensor_category = sensor_details["sensor_category"]
    sensor_meta = sensor_details["sensor_meta"]
    sensor_api_key = sensor_details["sensor_api_key"]
    result = sensor.insert_sensor(location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key)
    return jsonify(result)

@app.route("api/v1/sensor_data", methods=["POST"])
def insert_sensor_data():
    sensor_details = request.get_json()
    location_id = sensor_details["location_id"]
    sensor_name = sensor_details["sensor_name"]
    sensor_category = sensor_details["sensor_category"]
    sensor_meta = sensor_details["sensor_meta"]
    sensor_api_key = sensor_details["sensor_api_key"]
    result = sensor.insert_sensor(location_id, sensor_name, sensor_category, sensor_meta, sensor_api_key)
    return jsonify(result)

@app.route("api/v1/game", methods=["PUT"])
def update_game():
    game_details = request.get_json()
    id = game_details["id"]
    name = game_details["name"]
    price = game_details["price"]
    rate = game_details["rate"]
    result = game_controller.update_game(id, name, price, rate)
    return jsonify(result)


@app.route("api/v1/game/<id>", methods=["DELETE"])
def delete_game(id):
    result = game_controller.delete_game(id)
    return jsonify(result)


if __name__ == "__main__":
    create_tables()
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.run(host='0.0.0.0', port=8000, debug=False)
