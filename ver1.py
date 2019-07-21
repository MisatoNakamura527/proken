# センサから値を取って閾値以下ならlineに通知

import requests
import random
from grovepi import * 

moisture = 0
# A0に湿度センサ
dht_sensor_port = 7
#ポート7に温湿度センサー

# IFTTT_Webhook
def ifttt_webhook(eventid,value):
    payload = {"value1": value,
                "value2": "",
                "value3": "" }
    url = 'https://maker.ifttt.com/trigger/' + eventid + '/with/key/d1Ep3s3uUhMZugkBfz5vOQ'
    response = requests.post(url,payload)

# ここからスタート
if __name__ == '__main__':
        while True:
            try:
                [tmp, hum] = dht(dht_sensor_port, 1)
                soil_moisture = analogRead(moisture)
                print("temp = " + tmp + "C hum = " + hum + "%" )
                print("soil moisture(analog) = " +soil_moisture)

            except(IOError,TypeError) as e:
                print ("Error")
            if num == 77:
                print ("IFTTTへ送信")

                # IFTTT_Webhook
                # ifttt_webhook("python_test",num)
                ifttt_webhook("plant",num)

                print ("送信しました")
                break