from flask import Flask, render_template,redirect,request,session
from con_sql import con_to_sql
import os

app = Flask(__name__)
app.secret_key="dhawal123"

@app.route('/')
def home():
    return render_template ('home.html')
@app.route('/num')
def num():
    return render_template('num.html')
@app.route('/alpha')
def alpha():
    return render_template('alpha.html')
@app.route('/hindi')
def hindi():
    return render_template('hindi.html')
@app.route('/paint')
def paint():
    return render_template('paint.html')
@app.route('/cross')
def cross():
    return render_template('cross.html')
@app.route('/tech')
def tech():
    return render_template('tech.html')
@app.route('/rhym')
def rhym():
    return render_template('rhym.html')
@app.route('/poem')
def poem():
    return render_template('poem.html')

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form["name"]
    phone_no = request.form["phone_no"]
    email = request.form["email"]
    city_or_state = request.form["city_or_state"]

    conn = con_to_sql()      # DB connection
    cur = conn.cursor()     # cursor

    # 👉 PUT THIS HERE 👇
    cur.execute(
        "INSERT INTO users (name, phone_no, email, city_or_state) VALUES (%s, %s, %s, %s)",
        (name, phone_no, email, city_or_state)
    )

    conn.commit()            # save to DB
    cur.close()
    conn.close()

    return "Form submitted successfully"

@app.route("/create-table")
def create_table():
    try:
        conn = con_to_sql()
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            );
        """)

        conn.commit()
        cur.close()
        conn.close()

        return " TABLE CREATED SUCCESSFULLY"

    except Exception as e:
        return f" ERROR: {e}"
@app.route("/test-db")
def test_db():
    try:
        con_to_sql()
        return "DB CONNECTED"
    except Exception as e:
        return f"❌ {e}"

import psycopg2
import os
from urllib.parse import urlparse

def init_db():
    url = urlparse(os.environ["DATABASE_URL"])
    conn = psycopg2.connect(
        dbname=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port,
        sslmode="require"
    )

    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS contact_form (
            id SERIAL PRIMARY KEY,
            name TEXT,
            email TEXT,
            message TEXT
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
import psycopg2
import os
from urllib.parse import urlparse

def create_table():
    url = urlparse(os.environ["DATABASE_URL"])
    conn = psycopg2.connect(
        dbname=url.path[1:],
        user=url.username,
        password=url.password,
        host=url.hostname,
        port=url.port,
        sslmode="require"
    )
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT,
            phone_no TEXT,
            email TEXT,
            city_or_state TEXT
        );
    """)

    conn.commit()
    cur.close()
    conn.close()


# 🔹 CALL IT ONCE
create_table()



@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
     port = int(os.environ.get("PORT", 5000))
     app.run(host="0.0.0.0", port=port)

init_db()











