from db import get_db


def insert_location(company_id, location_name, location_country, location_city, location_meta):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO Location(company_id, location_name, location_country, location_city, location_meta) VALUES (?, ?, ?, ?, ?)"
    cursor.execute(statement, [company_id, location_name, location_country, location_city, location_meta])
    db.commit()
    return True


def update_location(id, company_id, location_name, location_country, location_city, location_meta):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE Location SET company_id = ?, location_name = ?, location_country = ?, location_city = ?, location_meta = ? WHERE id = ?"
    cursor.execute(statement, [company_id, location_name, location_country, location_city, location_meta, id])
    db.commit()
    return True


def delete_location(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM Location WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, company_id, location_name, location_country, location_city, location_meta FROM Location WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()


def get_locations(company_api_key):
    db = get_db()
    cursor = db.cursor()
    query = "SELECT Location.id, Location.company_id, Location.location_name, Location.location_country, Location.location_city, Location.location_meta FROM Location, Company  WHERE Location.company_id = Company.id AND Company.company_api_key = ? "
    cursor.execute(query, [company_api_key])
    return cursor.fetchall()
