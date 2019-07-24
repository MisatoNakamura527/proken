import time
import grovepi
import requests

# ifttt requests
url = 'https://maker.ifttt.com/trigger/plant/with/key/d1Ep3s3uUhMZugkBfz5vOQ'

#sensor port
moisture_sensor = 14 #A0

grovepi.pinMode(moisture_sensor,"INPUT")

while True:
    try:
        moisture_val = grovepi.analogRead(moisture_sensor)

        print("moisture = %d" %moisture_val)
        
        if moisture_val > 430:
            print("送信")
            response = requests.post(url)
            print("送信完了")

        time.sleep(1.0)

    except IOError:
        print("Error")
