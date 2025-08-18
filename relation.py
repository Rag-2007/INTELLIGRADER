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


