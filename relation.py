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
    
def create_relation():
    conn = postgre_connect()
    curs = conn.cursor()
    curs.execute("""
        CREATE TABLE IF NOT EXISTS relation(
            teacher_id varchar(255),
            teacher_dept varchar(255),
            roll varchar(255),
            marks varchar(255),
            suggest Text
        )
    """)
    conn.commit()
    conn.close()


def add_relation(id, dept, roll, marks, suggest):
    create_relation()
    conn = postgre_connect()
    curs = conn.cursor()
    curs.execute("""
        INSERT INTO relation VALUES(%s,%s,%s,%s,%s) 
    """, (id, dept, roll, marks, suggest))
    conn.commit()
    conn.close()


def search_relation(roll):
    create_relation()
    conn =postgre_connect()
    curs = conn.cursor()
    curs.execute("""
        SELECT teacher_dept,marks,suggest FROM relation WHERE roll = %s
    """, (roll,))
    response = curs.fetchall()
    conn.close()
    return response


