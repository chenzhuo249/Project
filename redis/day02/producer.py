import redis
import json

r = redis.Redis(host="127.0.0.1", port=6379, db=0, password="123456")

json_obj = {"task":"send_email", "from":"chenzhuo", "to":"huyue", "content":"i love you"}
json_str = json.dumps(json_obj)

r.lpush("pypc", json_str)

