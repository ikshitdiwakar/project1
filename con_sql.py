import mysql.connector
import os
from urllib.parse import urlparse

def con_to_sql():
    url = urlparse(os.environ.get("MYSQL_PUBLIC_URL"))

    return mysql.connector.connect(
        host=url.hostname,
        user=url.username,
        password=url.password,
        database=url.path.lstrip('/'),
        port=url.port
    )
