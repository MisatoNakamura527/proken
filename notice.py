import requests

# IFTTT_Webhook
def ifttt_webhook(eventid):
    payload = {"value1": "Internet",
                "value2": "Of",
                "value3": "Things" }
    url = 'https://maker.ifttt.com/trigger/' + eventid + '/with/key/d1Ep3s3uUhMZugkBfz5vOQ'
    response = requests.post(url, data=payload)
    print(response)

# ここからスタート
if __name__ == '__main__':
        print ("IFTTT連携開始")

        # IFTTT_Webhook
        ifttt_webhook("plant")

        print ("IFTTT連携終了")