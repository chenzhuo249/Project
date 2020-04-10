import redis

r = redis.Redis(host="127.0.0.1", port=6379, db=0, password="123456")

# r.sadd("pys1", "a", "b", "c", "d", "e")
# print(r.smembers("pys1"))


r.sadd("num1", 1, 2, 3)
r.sadd("num2", 1, 2, 4)
print(r.smembers("num1"))
print(r.smembers("num2"))
print(r.sdiff("num1", "num2"))








# 通用命令演示
# list_key = r.keys("*")
# for key in list_key:
#     print(key)

# list_l1 = r.lrange("l1", 0, -1)
# print(list(map(lambda x:x.decode(), list_l1)))

# print(r.exists("l1"))

# r.set("name", "chenzhuo")
# print(r.get("name").decode())

# r.mset({"n1":"chen", "n2":"hu", "n3":"zhuo"})
# print(list(map(lambda x:x.decode(),r.mget("n1", "n2", "n3"))))

# print(r.incr("a"))
# print(r.incrby("a", 10))

