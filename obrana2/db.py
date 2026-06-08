import mysql.connector
import json

db_conf = {
    "host":"localhost",
    "db_name": "zadatak",
    "user":"root",
    "passwd":""
}

def get_DB_connection():
    mydb = mysql.connector.connect(
        host=db_conf["host"],
        user=db_conf["user"],
        passwd=db_conf["passwd"],
        database=db_conf["db_name"]
    )
    return mydb

def create_session():
    mydb = get_DB_connection()
    cursor = mydb.cursor()

    cursor.execute("INSERT INTO sessions (data) VALUES (%s)", (json.dumps({}),))
    mydb.commit()

    session_id = cursor.lastrowid

    cursor.close()
    mydb.close()
    return session_id

def get_session(session_id):
    mydb = get_DB_connection()
    cursor = mydb.cursor()

    cursor.execute("SELECT session_id, data FROM sessions WHERE session_id=%s", (session_id,))

    result = cursor.fetchone()

    cursor.close()
    mydb.close()

    if result is None:
        return None, {}

    return result[0], json.loads(result[1])

def update_session(session_id, data):
    mydb = get_DB_connection()
    cursor = mydb.cursor()

    cursor.execute("UPDATE sessions SET data=%s WHERE session_id=%s", (json.dumps(data), session_id))
    mydb.commit()

    cursor.close()
    mydb.close()







    