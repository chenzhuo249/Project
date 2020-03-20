from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/ajax')
def ajax():
    return render_template('ajax.html')

@app.route('/ajax_server',methods=['get','post'])
def ajax_server():
    if request.method == 'GET':
        import time
        time.sleep(3)
        return json.dumps({"code":200,"msg":"OK"})
    elif request.method == 'POST':
        uname = request.json.get('uname')
        return json.dumps({"code":200,"msg":"欢迎%s"%uname})


if __name__ == "__main__":
    app.run(debug=True)