import mysql.connector
from urllib.parse import urlparse
import os

def con_to_sql():
    db_url = "mysql://root:pass@mysql.railway.internal:3306/railway"
    url = urlparse(db_url)

    return mysql.connector.connect(
        host=url.hostname,
        user=url.username,
        password=url.password,
        database=url.path.lstrip('/'),
        port=url.port
    )
