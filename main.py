import json
import requests
import os
import time
from datetime import datetime
from datetime import timedelta

bing_url = os.environ["bing_url"]
response = requests.get(bing_url)
data = json.loads(response.text)
bing_image_url = 'https://www.bing.com' + data['images'][0]['urlbase']+"_UHD.jpg"

# 添加时间戳
time_stamp = time.time()
utc_time = datetime.utcfromtimestamp(time_stamp)
time1 = str(utc_time + timedelta(hours=-7))

# 定义要发送的消息
message = {
      "content": "@everyone This is the Bing Daily image"+"\n Time(UTC-7):"+time1,
      "embeds": [
        {
          "image": {
            "url": bing_image_url
          }
        }
      ]
    }

# 定义请求头，包括机器人令牌和消息类型
bot_token = os.environ["bot_token"]
headers = {
    'Authorization': 'Bot ' + bot_token,
    'Content-Type': 'application/json'
}

# 定义请求 URL，包括要发送消息的频道 ID
discord_url = os.environ["discord_url"]
url = discord_url

# 发送 POST 请求，包括要发送的消息和请求头
response = requests.post(url, data=json.dumps(message), headers=headers)

# 打印响应
print(response.text)