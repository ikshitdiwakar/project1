import mysql.connector
import os
from urllib.parse import urlparse

def con_to_sql():
    db_url = os.environ.get("MYSQL_PUBLIC_URL")
    if not db_url:
        raise Exception("MYSQL_PUBLIC_URL not set")

    url = urlparse(db_url)

    return mysql.connector.connect(
        host=url.hostname,
        user=url.username,
        password=url.password,
        database=url.path.lstrip('/'),
        port=url.port
    )
