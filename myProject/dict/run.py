from flask import Flask, request, redirect, render_template
from dict_db import Database

db = Database()
db.create_cursor()
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index_view():
    return render_template('login.html')

@app.route("/login", methods=["GET", "POST"])
def login_view():
    name = request.form.get("userName", "xxx")
    pwd = request.form.get("userPassword", "xxx")
    # print(name, pwd)
    if db.s_login(name, pwd):
        # return "登录成功"
        return render_template('word.html')
    else:
        return "登录失败"

@app.route("/register", methods=["GET", "POST"])
def register_view():
    return render_template("register.html")

@app.route("/register2", methods=["GET", "POST"])
def register2_view():
    name = request.form.get("userName", "xxx")
    pwd = request.form.get("userPassword", "xxx")
    if db.s_register(name, pwd):
        return render_template('login.html')
    else:
        return "注册失败"



@app.route("/word", methods=["GET", "POST"])
def word_view():
    word = request.form.get("english", "xxx")
    return db.s_find(word)

if __name__ == "__main__":
    app.run(debug=True)



