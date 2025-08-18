import  psycopg2
import os
def postgre_connect():
    return psycopg2.connect(
        host= os.getenv('host'),
        port=os.getenv('port'),
        database=os.getenv('database'),
        user=os.getenv('user'),
        password=os.getenv('password')
    )
    

def create():
    conn = postgre_connect()
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS student (
            num SERIAL PRIMARY KEY ,
            rollno TEXT UNIQUE,
            password TEXT
        )
    ''')
    conn.commit()
    conn.close()

def add_val(rollno, password):
    create()
    conn = postgre_connect()
    cur = conn.cursor()
    try:
        cur.execute('''
            INSERT INTO student (rollno,password)
            VALUES (%s, %s)
        ''', (rollno, password))
        conn.commit()
        print("✅ student added successfully!")
    except psycopg2.IntegrityError as e:
        if "duplicate key value violates unique constraint" in str(e):
            print("⚠️ Duplicate entry! Teacher already exists.")
        else:
            print(f"❌ Integrity error: {e}")
    except Exception as e:
        print(f"❌ Error inserting data: {e}")
    finally:
        conn.close()

def search(rollno, password):
    create()
    conn = postgre_connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM student WHERE rollno=%s AND password=%s', (rollno, password))
    result = cur.fetchone()
    conn.close()
    return result

def fetch_rolls() :
    create()
    conn = postgre_connect()
    curs = conn.cursor()    
    curs.execute('SELECT rollno FROM student')
    res = curs.fetchall()
    conn.commit()
    conn.close()
    l=[]
    for r in res:
        l.append(r[0])
    return l

def search_roll(rollno):
    create()
    conn = postgre_connect()
    cur = conn.cursor()
    cur.execute('SELECT * FROM student WHERE rollno=%s', (rollno,))
    result = cur.fetchone()
    conn.close()
    return result
