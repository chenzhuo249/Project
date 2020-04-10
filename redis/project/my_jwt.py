import time, base64, json, hmac, copy

class Jwt:

    def __init__(self):
        pass

    @staticmethod
    def my_encode(my_payload, key, exp=300):
        # init header  json串中去掉多余空格，并且保持有序性
        header_json = json.dumps({"alg":"HS256", "typ":"JWT"}, separators=(",",":"), sort_keys=True)
        header_b64 = Jwt.my_b64_encode(header_json.encode())

        # init payload
        payload = copy.deepcopy(my_payload)
        payload["exp"] = time.time() + exp
        payload_json = json.dumps(payload, separators=(",",":"), sort_keys=True)
        payload_b64 = Jwt.my_b64_encode(payload_json.encode())

        # init sign
        hm = hmac.new(key.encode(), b".".join([header_b64, payload_b64]), digestmod="SHA256")
        hm_b64 = Jwt.my_b64_encode(hm.digest())

        return b".".join([header_b64, payload_b64, hm_b64])

    @staticmethod
    def my_b64_encode(b_s):
        return base64.urlsafe_b64encode(b_s).replace(b"=",b"")

    @staticmethod
    def my_b64_decode(b_s):
        rem = len(b_s) % 4
        if rem > 0:
            b_s += b"=" * (4 - rem)
        return base64.urlsafe_b64decode(b_s)


    @staticmethod
    def my_decode(token, key):
        header_b64, payload_b64, sign_b64 = token.split(b".")
        hm = hmac.new(key.encode(), b".".join([header_b64, payload_b64]), digestmod="SHA256")
        if Jwt.my_b64_encode(hm.digest()) != sign_b64:
            raise("signature 验证失败")

        #校验时间
        payload_json = Jwt.my_b64_decode(payload_b64)
        dict_payload = json.loads(payload_json.decode())
        exp = dict_payload["exp"]
        if time.time() > exp:
            raise("时间过期")
        return dict_payload

if __name__ == '__main__':
    t = Jwt()
    token = t.my_encode({"username":"chenzhuo"}, "hu", 3)
    print(token)
    # time.sleep(4)
    s = t.my_decode(token, "hu1")
    print(s)

