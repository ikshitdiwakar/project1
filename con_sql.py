import psycopg2
import os

def con_to_sql():
    return psycopg2.connect(
        os.getenv("DATABASE_URL"),
        sslmode="require"
    )


