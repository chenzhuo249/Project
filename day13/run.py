from flask import Flask, render_template, request, make_response
import json, os

app = Flask(__name__)

@app.route("/")
@app.route("/data")
def data_view():
    return render_template("cartData.html")


@app.route("/data_server")
def data_server_view():
    f = open("./static/cartData.txt", "r")
    data = f.read()
    f.close()
    return data


# method 2
# @app.route("/data_server")
# def data_server_view():
#     path = "./static/cartData.txt"
#     base_dir = os.path.dirname(__file__)
#     resp = make_response(open(os.path.join(base_dir, path)).read())
#     resp.headers["Content-type"]="text/plan;charset=UTF-8"
#     return resp

# method 3
# @app.route("/data_server")
# def ajax_test_add():
#     path = "./static/cartData.txt"
#     f_name = open(path, 'r', encoding='UTF-8').read()
#     return f_name
#     # return json.dumps({'content':f_name,'resCode':2000})

# method 3 原版
# @app.route('/getdata/md', methods=['post'])
# def ajax_test_add():
#     params = request.get_json()
#     childPath = params.get('title')
#     if(params.get('title') == None):
#         print('未传title字段！')
#         return json.dumps({'resCode':'4001','msg':'参数错误title为必传'})
#     else:
#         path = './static' + childPath + '.md'
#         try:
#             f_name = open(path, 'r', encoding='UTF-8').read()
#             print(f_name)
#             # 成功获取到md文件内容啦
#             return json.dumps({'content':f_name,'resCode':2000})
#         except OSError as reason:
#             print('读取文件出错了T_T')
#             print('出错原因是%s' % str(reason))
#         return json.dumps({'err': str(reason),'resCode':5000})
        
        
if __name__ == "__main__":
    app.run(debug=True)
