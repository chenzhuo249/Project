from test_celery.celery import app
import time

@app.task
def task_test():
    print("task begin....")
    time.sleep(5)
    print("task over....")

