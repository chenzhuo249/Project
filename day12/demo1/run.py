from flask import Flask, request, render_template

app = Flask(__name__)

# @app.route("/post")
# def post_view():
#     return render_template("ajax_post.html")

# @app.route("/post_server", methods=["POST"])
# def post_server_view():
#     name = request.form.get("uname")
#     return "欢迎" + name + "访问!"


@app.route("/post", methods=["GET", "POST"])
def post_view():
    if request.method == "GET":
        return render_template("ajax_post.html")
    elif request.method == "POST":
        name = request.form.get("uname")
        return "欢迎" + name + "访问!" 



if __name__ == "__main__":
    app.run(debug=True)