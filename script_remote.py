import requests
from bs4 import BeautifulSoup
import json
import random
import datetime
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
    for i in range(8):
        tmp = get_query(400*i, 400*(i+1)-1)
        message.append(tmp)
    post_message(message)

def get_query(low, hi):
    # print(str(title))
    lst = []
    for info in dataset:
        try:
            tmp = dataset[info]["difficulty"]
            if (low <= int(dataset[info]["difficulty"]) and int(dataset[info]["difficulty"]) <= hi):
                lst.append(str(info))
        except KeyError:
            continue            

    return (lst[random.randint(0,len(lst))])

def post_message(message):
    # sends message to discord server
    payload = {
        "username" : "Daily Problemset",
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
            "name": f"Q{i+1}: ",
            "value": f"[{message[i]}](https://atcoder.jp/contests/{message[i][0:len(message[i])-2]}/tasks/{message[i]})",
            # "inline": "false"
        })

    with requests.post(WEBHOOK_URL, json=payload) as response :
        print(response.status_code)
    
if __name__ == "__main__":
    main()