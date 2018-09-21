# -*- coding: utf-8 -*-
import base64
import json
import time
import hashlib
import urllib.request
import urllib.parse

# API请求地址、API KEY、APP ID等参数，提前填好备用
api_url = "http://api.xfyun.cn/v1/service/v1/tts"
API_KEY = "76924c69985340dfa9d1a35c18741994"
APP_ID = "5b9c95dd"
OUTPUT_FILE = "F:/Python/Django/PeopleAttitude/Web/views/method/link/out.mp3"  # 输出音频的保存路径，请根据自己的情况替换
TEXT = "苟利国家生死以，岂因祸福避趋之，知道了没，出音频的保存路径，请根据自己的情况替换。留白"

# 构造输出音频配置参数
Param = {
    "auf": "audio/L16;rate=16000",  # 音频采样率
    "aue": "lame",  # 音频编码，raw(生成wav)或lame(生成mp3)
    "voice_name": "xiaoyan",
    "speed": "50",  # 语速[0,100]
    "volume": "77",  # 音量[0,100]
    "pitch": "50",  # 音高[0,100]
    "engine_type": "aisound"  # 引擎类型。aisound（普通效果），intp65（中文），intp65_en（英文）
}
# 配置参数编码为base64字符串，过程：字典→明文字符串→utf8编码→base64(bytes)→base64字符串
Param_str = json.dumps(Param)  # 得到明文字符串
Param_utf8 = Param_str.encode('utf8')  # 得到utf8编码(bytes类型)
Param_b64 = base64.b64encode(Param_utf8)  # 得到base64编码(bytes类型)
Param_b64str = Param_b64.decode('utf8')  # 得到base64字符串

# 构造HTTP请求的头部
time_now = str(int(time.time()))
checksum = (API_KEY + time_now + Param_b64str).encode('utf8')
checksum_md5 = hashlib.md5(checksum).hexdigest()
header = {
    "X-Appid": APP_ID,
    "X-CurTime": time_now,
    "X-Param": Param_b64str,
    "X-CheckSum": checksum_md5
}

# 构造HTTP请求Body
body = {
    "text": TEXT
}
body_urlencode = urllib.parse.urlencode(body)
body_utf8 = body_urlencode.encode('utf8')

# 发送HTTP POST请求
req = urllib.request.Request(api_url, data=body_utf8, headers=header)
response = urllib.request.urlopen(req)

# 读取结果
response_head = response.headers['Content-Type']
if (response_head == "audio/mpeg"):
    with open(OUTPUT_FILE, "wb") as f:
        data = response.read()  # a 'bytes' object\
        f.write(data)
    print('输出文件: ' + OUTPUT_FILE)
else:
    print('错误')
    print(response.read().decode('utf8'))
