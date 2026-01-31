import pyodbc

def con_to_sql():
    try:
        conn=pyodbc.connect('DRIVER={SQL Server};'
                            'SERVER=DESKTOP-DNPGNND\SQLEXPRESS;'
                            'DATABASE=funlearn;'
                            'Trusted_Connection=yes')
        return conn
    except Exception as e:
        return None