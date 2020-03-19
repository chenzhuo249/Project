from flask import Flask, request, redirect, render_template
from dict_db import Database
import json

db = Database()
# 生成游标
# db.create_cursor()

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index_view():
    return render_template("index.html")

@app.route("/index_data", methods=["POST"])
def index_data_view():
    name = request.json.get("name")
    pwd = request.json.get("password")
    return "登录结果"+ name + pwd


@app.route("/register")
def register_view():
    return render_template("register.html")

@app.route("/register_data", methods=["POST"])
def register_data_view():
    name = request.json.get("name")
    pwd = request.json.get("password")
    return "注册结果"+ name + pwd


@app.route("/dict")
def dict_view():
    return render_template("dict.html")

@app.route("/dict_data")
def dict_data_view():
    return "查询结果"


if __name__ == "__main__":
    app.run(debug=True)



