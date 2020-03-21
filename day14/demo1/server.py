from flask import Flask, render_template

app = Flask(__name__)


@app.route("/server")
def index_view():
    return '{"data": "跨域成功"}'

if __name__ == "__main__":
    app.run(debug=True, port=5001)