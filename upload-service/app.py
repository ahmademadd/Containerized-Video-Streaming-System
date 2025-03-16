from flask import Flask, redirect, url_for, render_template, request, flash, session
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
from flask_session import Session
import time
import redis
import os
app = Flask(__name__)

app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = True
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_KEY_PREFIX'] = 'flask_session:'
app.config['SESSION_REDIS'] = redis.StrictRedis(host='redis', port=6379, db=0)
app.config['SECRET_KEY'] = 'secret'
app.secret_key = 'secret'
Session(app)

app.config['MYSQL_HOST'] = 'db'
app.config['MYSQL_USER'] = 'user'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'flaskapp'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

UPLOAD_FOLDER = "/videos"

@app.route('/upload', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        file = request.files['filename']
        
        cur = mysql.connection.cursor()
        cur.execute("SELECT id FROM users WHERE username = %s", (session['username'],))
        user = cur.fetchone()
        user_id = user['id']
        
        cur.execute("INSERT INTO uploads (filename, user_id) VALUES (%s, %s)", (file.filename, user_id))
        mysql.connection.commit()

        filepath = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(filepath)

        cur.close()
        return redirect("http://localhost:5002/stream")
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
