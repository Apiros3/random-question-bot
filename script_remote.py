import requests
from bs4 import BeautifulSoup
import json
import random
import datetime
import os
# import discord

WEBHOOK_URL = os.environ["WEBHOOK"]

url = "https://kenkoooo.com/atcoder/resources/problem-models.json"

response = requests.get(url)
# print(response.content)
soup = BeautifulSoup(response.content, 'lxml')
dataset = json.loads(soup.get_text())
# diff = ["\u26AA","\uD83D\uDFE4","\uD83D\uDFE2",""]

def main():
    print("running...")

    message = []
    diff = []
    for i in range(8):
        tmp = get_query(400*i, 400*(i+1)-1)
        message.append(tmp[0])
        diff.append(tmp[1])
    post_message(message,diff)

def get_query(low, hi):
    # print(str(title))
    lst = []
    diff = []
    for info in dataset:
        try:
            tmp = dataset[info]["difficulty"]
            if (low <= int(dataset[info]["difficulty"]) and int(dataset[info]["difficulty"]) <= hi):
                lst.append(str(info))
                diff.append(str(tmp))
        except KeyError:
            continue            

    rnd = random.randint(0,len(lst))
    return (lst[rnd], diff[rnd])

def post_message(message,diff):
    # sends message to discord server
    payload = {
        "username" : "AtCoder Daily Problemset",
        # "avatar_url" : "https://github.com/Apiros3/Apiros3.github.io/blob/main/personal/img/100747246.jpeg",
        "embeds" : [
            {
                "title": f"Problemset for {datetime.datetime.today().strftime('%Y-%m-%d')}",
                "description": "",
                "color" : "002147",
                "fields" : []
            }
        ]
    }
    for i in range(8):
        payload["embeds"][0]["fields"].append({
            "name": f"Q{i+1}: (diff: {diff[i]})",
            "value": f"[{message[i]}](https://atcoder.jp/contests/{message[i][0:len(message[i])-2]}/tasks/{message[i]})",
            # "inline": "false"
        })

    with requests.post(WEBHOOK_URL, json=payload) as response :
        print(response.status_code)
    
if __name__ == "__main__":
    main()
