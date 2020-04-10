import json

import redis

r = redis.Redis(host="127.0.0.1", port=6379, db=0, password="123456")

while True:
    woker = r.brpop("pypc", 5)
    print(woker)
    if woker:
        json_obj = json.loads(woker[1])
        print(json_obj)
