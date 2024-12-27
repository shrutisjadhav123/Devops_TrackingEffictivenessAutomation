import sqlite3

class Database:
    def __init__(self, db_file='devops_metrics.db'):
        self.conn = sqlite3.connect(db_file)
        self.create_table()

    def create_table(self):
        with self.conn:
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS metrics (
                    id INTEGER PRIMARY KEY,
                    timestamp TEXT,
                    lead_time REAL,
                    change_failure_rate REAL,
                    deployment_frequency INTEGER,
                    mttr REAL
                )
            ''')

    def insert_metrics(self, lead_time, change_failure_rate, deployment_frequency, mttr):
        with self.conn:
            self.conn.execute('''
                INSERT INTO metrics (timestamp, lead_time, change_failure_rate, deployment_frequency, mttr)
                VALUES (datetime('now'), ?, ?, ?, ?)
            ''', (lead_time, change_failure_rate, deployment_frequency, mttr))

    def close(self):
        self.conn.close()