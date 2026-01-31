from flask import Flask, render_template,redirect,request,session
from con_sql import con_to_sql


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

@app.route('/submit',methods=['GET','POST'])
def submit():
    if request.method=='POST':
        name=request.form['name']
        pno=request.form['pno']
        email=request.form['email']
        city=request.form['city']
        gen=request.form['gender']
        conn=con_to_sql()
        cursor=conn.cursor()
        cursor.execute("INSERT INTO fun_and_learn (Name,Phone_No,Email,City_or_State,Gender) VALUES(?,?,?,?,?)",(name,pno,email,city,gen))
        conn.commit()
        session['name']=name
        session['pno']=pno
        session['email']=email
    return render_template('home.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000 ,debug=True)
