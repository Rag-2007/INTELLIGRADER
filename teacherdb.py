import  psycopg2
import streamlit as st

def postgre_connect():
    return psycopg2.connect(
        host= st.secrets['host'],
        port=st.secrets['port'],
        database=st.secrets['database'],
        user=st.secrets['user'],
        password=st.secrets['password']
    )
    
def create():
    conn = postgre_connect()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS teacher (
            num SERIAL PRIMARY KEY ,
            id TEXT UNIQUE,
            password TEXT,
            dept TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_val(id, password, dept):
    create()
    conn = postgre_connect()
    cur = conn.cursor()
    try:
        cur.execute('''
            INSERT INTO teacher (id, password, dept)
            VALUES (%s, %s, %s)
        ''', (id, password, dept))
        conn.commit()
        print("✅ Teacher added successfully!")
    except psycopg2.IntegrityError as e:
        if isinstance(e, psycopg2.errors.UniqueViolation):
            print("⚠️ Duplicate entry! Teacher already exists.")
        else:
            print(f"❌ Integrity error: {e}")
    except Exception as e:
        print(f"❌ Error inserting data: {e}")
    finally:
        conn.close()

def search(id):
    create()
    conn = postgre_connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM teacher WHERE id=%s', (id,))
    result = cur.fetchone()
    conn.close()
    return result
def search_login(id,password):
    create()
    conn = postgre_connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM teacher WHERE id=%s and password=%s', (id,password))
    result = cur.fetchone()
    conn.close()
    return result


