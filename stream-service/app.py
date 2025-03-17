from flask import Flask, Response, render_template, session, request
from flask_mysqldb import MySQL
from flask_session import Session
import os
import redis

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

VIDEO_DIR = "/videos"

@app.route('/stream')
def index():
    username = session['username']
    cur = mysql.connection.cursor()

    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    user = cur.fetchone()
    user_id = user['id']

    cur.execute("SELECT filename FROM uploads WHERE user_id = %s", (user_id,))
    vid = [row['filename'] for row in cur.fetchall()]
    cur.close()

    selectedvideo = request.args.get('filename', None)

    return render_template('index.html', videos=vid, selected_video=selectedvideo)

@app.route('/stream/<filename>')
def stream_video(filename):
    file_path = os.path.join(VIDEO_DIR, filename)
    def generate():
        with open(file_path, "rb") as video:
            chunk_size = 1024 * 1024
            while chunk := video.read(chunk_size):
                yield chunk

    return Response(generate(), content_type="video/mp4")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)