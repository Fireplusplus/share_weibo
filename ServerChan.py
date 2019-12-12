import requests
import json

def infoReq(res):
    print(res.text)

def sendNotify(title, content):
    api = "https://sc.ftqq.com/SCU68512T4adba4e6a033e0aded8c0587aa1400585df0fda467b05.send"
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

