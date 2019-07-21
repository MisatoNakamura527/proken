import requests

url = 'https://maker.ifttt.com/trigger/python_test/d1Ep3s3uUhMZugkBfz5vOQ'

print("送信")
response = requests.post(url)
print("送信完了")