from db import get_db


def insert_company(company_name, company_api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO Company(company_name, company_api_key) VALUES (?, ?)"
    cursor.execute(statement, [company_name, company_api_key])
    db.commit()
    return True


def update_company(id, company_name, company_api_key):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE Company SET company_name = ?, company_api_key = ? WHERE id = ?"
    cursor.execute(statement, [company_name, company_api_key, id])
    db.commit()
    return True


def delete_company(id):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM Company WHERE id = ?"
    cursor.execute(statement, [id])
    db.commit()
    return True


def get_by_id(id):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT id, company_name, company_api_key FROM Company WHERE id = ?"
    cursor.execute(statement, [id])
    return cursor.fetchone()


def get_companies():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT id, company_name, company_api_key FROM Company"
    cursor.execute(query)
    return cursor.fetchall()
