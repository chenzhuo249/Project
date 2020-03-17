from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index_view():
    return render_template("index.html")

@app.route("/demo1")
def demo1_view():
    info = request.args.get("info", "404")
    return "查询" + info + "结果"

if __name__ == "__main__":
    app.run(debug=True)