from flask import Flask
from flask import render_template#响应模板的函数
from flask import request#请求对象 包含前端所有和请求有关的数据
app = Flask(__name__)

#http://127.0.0.1:5000/
@app.route('/')
def index_view():
    return render_template('homework.html')


@app.route('/server')
def server():
    kw = request.args.get('kw')#python
    search_list = ['的历史','简介','官网','发展前景']
    #data = 'python的历史|python简介|python官网|python发展前景|'
    data = ''
    for i in search_list:
        data += kw+i+'|'
    return data.strip("|")




if __name__ == "__main__":
    app.run(debug=True)