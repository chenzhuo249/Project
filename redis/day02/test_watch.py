import time
import redis

pool = redis.ConnectionPool(host="127.0.0.1", port=6379, db=0, password="123456")
r = redis.Redis(connection_pool=pool)

def double_accout(user_id):

    key = f"ac_{user_id}"
    with r.pipeline() as pipe:
        while True:
            try:
                pipe.watch(key) # 直接发给redis
                money = int(r.get(key))
                print(money)

                pipe.multi()
                time.sleep(5)
                pipe.set(key, money * 2)
                pipe.execute()
                print("----success-----")
                break
            except redis.WatchError:
                print("--------key changed--------")
                continue


if __name__ == '__main__':
    double_accout("chen")










