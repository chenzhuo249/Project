import redis

pool = redis.ConnectionPool(host = '127.0.0.1',db=0,port=6379,password="123456")
r = redis.Redis(connection_pool=pool)

# def 函数装饰器名称(func):
#     def 内嵌函数(*args, **kwargs):
#         需要添加的新功能
#         return func(*args, **kwargs)
#     return 内嵌函数

def cul_time(func):
    def package(*args, **kwargs):
        import time
        start = time.perf_counter()
        fu = func(*args, **kwargs)
        end = time.perf_counter()
        print(func.__name__, end - start)
        return fu
    return package


@cul_time
def withpipeline(r):
    p = r.pipeline()
    for i in range(1000):
        key = 'test1' + str(i)
        value = i+1
        p.set(key, value)
    p.execute()

@cul_time
def withoutpipeline(r):
    for i in range(1000):
        key = 'test2' + str(i)
        value = i+1
        r.set(key, value)

if __name__ == '__main__':
    withpipeline(r)
    withoutpipeline(r)