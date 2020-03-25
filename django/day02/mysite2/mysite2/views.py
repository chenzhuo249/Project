from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render


def test_html(request):
    # t = loader.get_template("index.html")
    # html = t.render()
    # return HttpResponse(html)
    dic = {
        # "name": "chenzhuo",
        # "age": 18,
        # "person": {
        #     "name": "胡月",
        #     "age": 16
        # },
        "score": [91, 92, 93, 94]
    }

    return render(request, "index.html", dic)



def mycal_view(request):
    if request.method == "GET":
        return render(request, "mycal.html")
    elif request.method == "POST":
        dict_op = {"add": "+", "sub": "-", "mul": "*", "div": "/"}
        x = request.POST.get("x", "not found")
        op = request.POST.get("op", "not found")
        y = request.POST.get("y", "not found")
        if x == "not found" or op == "not found" or y == "not found":
            return HttpResponse("valueError!!!")
        else:
            res = eval(x + dict_op[op] + y)
            # dic = {
            #     "x": x,
            #     "op": op,
            #     "y": y,
            #     "res": result
            # }
        return render(request, "mycal.html", locals())

