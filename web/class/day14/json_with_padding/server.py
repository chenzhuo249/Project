from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route("/server")
def index_view():
    name = request.args.get("callback")
    data = {"code":200, "data": "跨域成功"}
    return name + "(" + json.dumps(data) + ")"
    # return json.dumps(data)

if __name__ == "__main__":
    app.run(debug=True, port=5001)