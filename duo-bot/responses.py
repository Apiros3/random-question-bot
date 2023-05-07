import random 
import bot 
import discord

def handle_reesponse(message) -> str:
    p_message = message.lower()
    if p_message[0:6] == 'random':
        for i in range(7,len(p_message)):
            if p_message[i] == " ":
                # print(p_message[7:i])
                # print(p_message[i+1:])
                low = int(p_message[7:i])
                hi = int(p_message[i+1:])
                problem = bot.get_query(low,hi)
                embed = discord.Embed(color=0x002147)
                embed.title = f"Random Question in Range [{low},{hi}]"
                embed.description = f"Problem: {problem[0]}\nDifficulty: {problem[1]}"
                embed.add_field(name="Link:", value=f"https://atcoder.jp/contests/{problem[0][0:len(problem[0])-2]}/tasks/{problem[0]}")

                return embed    
        return "Invalid input. Do '!help --api3' to receive help"
    if p_message == '!help':
        embed = discord.Embed(color=0x002147)
        embed.title = "Help Menu"

        embed.add_field(name="?command", value="Does 'command' and sends result via PM", inline="False")
        embed.add_field(name="random low high", value="Sends a random AtCoder problem with difficulty between low and high (inclusive)", inline="False")            
        embed.add_field(name="!help", value="Shows this help menu", inline="False")
            
        return embed
    
    return ''