import datetime
import time

from django.http import HttpResponse

from myCelery.celery_worker import app


@app.task
def task_test():
    print("task begin....")
    time.sleep(10)
    print("task over....")

def index_view(request):
    task_test.delay()
    now = datetime.datetime.now()
    html = "return at %s" % (now.strftime('%H:%M:%S'))
    return HttpResponse(html)

