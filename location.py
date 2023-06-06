from db import get_db
from flask import jsonify
import admin

def insert_location(company_id, location_name, location_country, location_city, location_meta, company_api_key):
    key = jsonify({"company_id":company_id,"company_api_key":company_api_key})
    data = admin.get_by_id(company_id,company_api_key)
    if(data == key):
        db = get_db()
        cursor = db.cursor()
        statement = "INSERT INTO Location(company_id, location_name, location_country, location_city, location_meta) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(statement, [company_id, location_name, location_country, location_city, location_meta])
        db.commit()
        return True
    else: 
        return False
    
def update_location(id, company_id, location_name, location_country, location_city, location_meta, company_api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "WITH Company(id, company_api_key), Location(company_id) UPDATE Location SET Location.company_id = ?, Location.location_name = ?, Location.location_country = ?, Location.location_city = ?, Location.location_meta = ? WHERE Location.id = ? AND Location.company_id = Company.id AND Company.company_api_key = ?"
    cursor.execute(statement, [company_id, location_name, location_country, location_city, location_meta, id, company_api_key])
    db.commit()
    return True


def delete_location(id, company_api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "WITH Company(id,company_api_key), Location(id,company_id) DELETE FROM Location WHERE Location.id = ? AND Location.company_id = Company.id AND Company.company_api_key = ?"
    cursor.execute(statement, [id, company_api_key])
    db.commit()
    return True


def get_by_id(id, company_api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "WITH Company(id,company_api_key), Location(id,company_id) SELECT Location.id, Location.company_id, Location.location_name, Location.location_country, Location.location_city, Location.location_meta FROM Location WHERE Location.id = ? AND Location.company_id = Company.id AND Company.company_api_key = ?"
    cursor.execute(statement, [id, company_api_key])
    return cursor.fetchone()


def get_locations(company_api_key):
    db = get_db()
    cursor = db.cursor()
    query = "WITH Company(id,company_api_key), Location(id,company_id) SELECT Location.id, Location.company_id, Location.location_name, Location.location_country, Location.location_city, Location.location_meta FROM Location WHERE Location.company_id = Company.id AND Company.company_api_key = ? "
    cursor.execute(query, [company_api_key])
    return cursor.fetchall()