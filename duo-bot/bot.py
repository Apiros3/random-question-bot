#bot.py
#install link: https://discord.com/api/oauth2/authorize?client_id=1104508299094806669&permissions=8&scope=bot

import discord
import responses
import random
import requests
from bs4 import BeautifulSoup
import json 
# import os

url = "https://kenkoooo.com/atcoder/resources/problem-models.json"

response = requests.get(url)
# print(response.content)
soup = BeautifulSoup(response.content, 'lxml')
dataset = json.loads(soup.get_text())
# diff = ["\u26AA","\uD83D\uDFE4","\uD83D\uDFE2",""]

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

    rnd = random.randint(0,len(lst)-1)
    return (lst[rnd], diff[rnd])


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_reesponse(user_message)
        # if (response == "") break
        if response != "":
            await message.author.send(embed=response) if is_private else await message.channel.send(embed=response)
    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN = '...'

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')
    
    @client.event 
    async def on_message(message):
        if message.author == client.user:
            return 
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message,user_message,is_private=False)

    client.run(TOKEN)

