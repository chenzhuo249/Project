from flask import Flask, request, redirect, render_template
from dict_db import Database
import json

db = Database()
# 生成游标
db.create_cursor()

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index_view():
    return render_template("index.html")
# 登录逻辑处理
@app.route("/index_data", methods=["POST"])
def index_data_view():
    name = request.json.get("name")
    pwd = request.json.get("password")
    if db.s_login(name, pwd):
        return '{"code":77, "msg":"登录成功,可跳转到 dict.html页面"}'
    else:
        return '{"code":44, "msg":"登录失败"}'
    


@app.route("/register")
def register_view():
    return render_template("register.html")
# 注册逻辑处理
@app.route("/register_data", methods=["POST"])
def register_data_view():
    name = request.json.get("name")
    pwd = request.json.get("password")
    if db.s_register(name, pwd):
        return '{"code":77, "msg":"注册成功,可跳转到 index.html登录页面"}'
    else:
        return '{"code":44, "msg":"注册失败"}'


@app.route("/dict")
def dict_view():
    return render_template("dict.html")
# 查询单词逻辑处理
@app.route("/dict_data")
def dict_data_view():
    return "查询结果"


if __name__ == "__main__":
    app.run(debug=True)



