import requests
import random

# IFTTT_Webhook
def ifttt_webhook(eventid,value):
    payload = {"value1": value,
                "value2": "Of",
                "value3": "Things" }
    url = 'https://maker.ifttt.com/trigger/' + eventid + '/with/key/d1Ep3s3uUhMZugkBfz5vOQ'
    response = requests.post(url,payload)

# ここからスタート
if __name__ == '__main__':
        while True:
            num = random.randint(0,100)
            print(num)
            if num == 77:
                print ("IFTTTへ送信")

                # IFTTT_Webhook
                ifttt_webhook("python_test",num)
                ifttt_webhook("plant",num)

                print ("送信しました")
                break