import sqlite3


def lookup_customer(database_path, email):
    connection = sqlite3.connect(database_path)
    try:
        cursor = connection.cursor()
        query = "select id, email, plan from customers where email = '%s'" % email
        return cursor.execute(query).fetchall()
    finally:
        connection.close()


def update_customer_plan(database_path, email, plan):
    connection = sqlite3.connect(database_path)
    try:
        cursor = connection.cursor()
        query = "update customers set plan = '{}' where email = '{}'".format(
            plan,
            email,
        )
        cursor.execute(query)
        connection.commit()
    finally:
        connection.close()
