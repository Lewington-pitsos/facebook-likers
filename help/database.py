import psycopg2

conn_str = "dbname='facebook_comments' user='postgres'" # Might want to change this

def truncate(value: str, length: int) -> str:
    if len(value) > length:
        return value[:length] + "..."
    
    return value


class db:
    def __init__(self):
        self.connection = psycopg2.connect(conn_str)
        self.cursor = self.connection.cursor()

    def commit(self):
        self.connection.commit()
    
    def rollback(self):
        self.connection.rollback()
    
    def save_link(self, link: str, link_type: str, bad: bool=False):
        good = 0 if bad else 1
        bad = 1 - good

        self.cursor.execute("""
        INSERT INTO links_encountered (link_type, outer_html, good, bad)
        VALUES(%s, %s, %s, %s)
        ON CONFLICT (link_type, outer_html) DO UPDATE SET good = links_encountered.good + %s, bad = links_encountered.bad + %s
        RETURNING id;""", (link_type, truncate(link, 450), good, bad, good, bad))
        self.commit()