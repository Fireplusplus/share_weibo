import requests
import json

def infoReq(res):
    print(res.text)

def sendNotify(title, content):
    api = "https://sc.ftqq.com/xxxxxxxxxxxxxxxxxxxxxxxx.send"
    data = {
        "text":title,
        "desp":content
    }

    res = requests.post(api,data = data)
    infoReq(res)

if __name__ == '__main__':
    title = input("Input title:")
    content = input("Input content:")
    sendNotify(title, content)

