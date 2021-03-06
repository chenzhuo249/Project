import json
import base64
import time
import hmac
import copy

class Jwt():

    def __init__(self):
        pass


    @staticmethod
    def encode(my_payload, key, exp=300):

        #init header
        header = {'typ': 'JWT', 'alg': 'HS256'}
        header_json = json.dumps(header, separators=(',',':'), sort_keys=True)
        #separators: 第一个参数为 每个键值对之间拿什么分割， 第二个参数为每个键与值之间拿什么分割
        header_bs = Jwt.b64encode(header_json.encode())

        #init payload
        payload = copy.deepcopy(my_payload)
        payload['exp'] = time.time() + exp
        payload_json = json.dumps(payload, separators=(',',':'),sort_keys=True)
        payload_bs = Jwt.b64encode(payload_json.encode())

        # init sign
        hm = hmac.new(key.encode(), header_bs + b'.' + payload_bs, digestmod='SHA256')
        hm_bs = Jwt.b64encode(hm.digest())

        return header_bs + b'.' + payload_bs + b'.' + hm_bs

    @staticmethod
    def b64encode(j_s):

        return base64.urlsafe_b64encode(j_s).replace(b'=', b'')




if __name__ == '__main__':

    s = Jwt.encode({'username':'guoxiaonao'}, 'abcdef')
    #b'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE1ODY1MDkwODYuMTQ5NTUzOCwidXNlcm5hbWUiOiJndW94aWFvbmFvIn0.ZWjPO6Lha8M7PHolIxdvH-iUih5NWk6cWbKTfZoH7lE'

    print(s)

























