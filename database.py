import sqlite3
import pandas as pd

DB_NAME = "ids_security_events.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS security_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            src_ip TEXT,
            dst_ip TEXT,
            protocol TEXT,
            dst_port INTEGER,
            packet_count INTEGER,
            byte_count INTEGER,
            duration REAL,
            flags TEXT,
            label TEXT,
            classification TEXT,
            severity TEXT,
            risk_score INTEGER,
            triggered_rules TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_events_to_db(df):
    init_db()
    conn = sqlite3.connect(DB_NAME)
    df.to_sql('security_events', conn, if_exists='replace', index=False)
    conn.close()

def load_events_from_db():
    init_db()
    conn = sqlite3.connect(DB_NAME)
    df = pd.read_sql('SELECT * FROM security_events', conn)
    conn.close()
    return df
