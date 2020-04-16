# 创建 tasks.py 文件

from celery import Celery

# 初始化celery, 指定broker
app = Celery('chenzhuo', broker='redis://:@127.0.0.1:6379/1')


#  broker='redis://:密码@IP地址:端口/库'
# 若redis无密码，password可省略
# app = Celery('guoxiaonao', broker='redis://:@127.0.0.1:6379/1')

# 创建任务函数
@app.task
def task_test():
    print("-----test woker-----------")
