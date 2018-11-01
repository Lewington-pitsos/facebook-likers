import psycopg2
import requests
import platform
from psycopg2 import extras

conn_str = "dbname='facebook_comments' user='postgres'" # Might want to change this

def truncate(value: str, length: int) -> str:
    if len(value) > length:
        return value[:length] + "..."
    
    return value


class db:
    def __init__(self):
        self.connection = psycopg2.connect(conn_str)
        self.cursor = self.connection.cursor(cursor_factory=extras.DictCursor)

    def commit(self):
        self.connection.commit()
    
    def rollback(self):
        self.connection.rollback()
    
    def save_link(self, link: str, link_type: str, bad_link: bool=False):
        bad = 1 if bad_link else 0
        good = 1 - bad

        self.cursor.execute("""
        INSERT INTO links_encountered (link_type, outer_html, good, bad)
        VALUES(%s, %s, %s, %s)
        ON CONFLICT (link_type, outer_html) DO UPDATE SET good = links_encountered.good + %s, bad = links_encountered.bad + %s
        RETURNING id;""", (link_type, truncate(link, 450), good, bad, good, bad))
        self.commit()

    def save_user(self, details: dict):
        self.cursor.execute("""
        INSERT INTO fake_users (first_name, last_name, birth_day, birth_month, birth_year, pass, temp_mail, ip, computer_name) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            details["first_name"],
            details["last_name"],
            details["birth_day"],
            details["birth_month"],
            details["birth_year"],
            details["password"],
            details["mail"],
            requests.get('http://ip.42.pl/raw').text,
            platform.node(),
        ))
        self.commit()
    
    def choose_fake_user(self):
        self.cursor.execute("""
        SELECT * FROM fake_users ORDER BY times_used ASC LIMIT 1
        """)
        return self.cursor.fetchone()
    
    def record_fake_user_use(self, user_id: int):
        self.cursor.execute("""
        UPDATE fake_users SET times_used = fake_users.times_used + 1 WHERE id = %s
        """, (user_id,))