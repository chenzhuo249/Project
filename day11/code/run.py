from flask import Flask, request,render_template

# tempaltes 默认的模板目录,存放页面
# static 默认的静态资源目录,存放静态文件, img/js/css ...
app = Flask(__name__)

@app.route("/demo")
def demo1_view():
    return render_template("demo1.html")

@app.route("/server")
def server_view():
    return render_template("demo2.html")

@app.route("/exer_server")
def exer_view():
    name = request.args.get("name", "xxx")
    return name + "加油, 你会成功的!"

@app.route("/login")
def login_view():
    return render_template("demo3.html")

list01 = ["chen", "hu"]
@app.route("/logins")
def login2_view():
    name = request.args.get("name")
    password = request.args.get("password")
    for item in list01:
        if item == name:
            return "NO"
    list01.append(name)
    return "YES"
        



if __name__ == "__main__":
    app.run(debug=True)