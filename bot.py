import os

import discord
from dotenv import load_dotenv

from intents.fun_fact import check_for_fun_fact
from intents.goodbye import check_for_goodbye
from intents.google import send_google_link
from intents.hello import check_for_hello
from intents.mem import check_for_meme
from intents.music import check_for_music
from intents.thanks import check_for_thanks
from intents.time import check_for_time
from intents.weather import check_for_weather
from intents.whats_up import check_for_whats_up
from intents.who_are_you import check_for_who_are_you

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Witaj na serwerze, {member.name}!'
    )


@client.event
async def on_message(message):
    if message.channel.name == os.getenv('DISCORD_CHANNEL') and message.author.bot == False:
        print(message.author.display_name + ": " + message.content)
        message.content = message.content.lower()
        answered = False

        reply = check_for_hello(message)
        if reply != "":
            await message.channel.send(reply)
            answered = True

        reply = check_for_who_are_you(message)
        if reply != "":
            await message.channel.send(reply)
            answered = True

        reply = check_for_fun_fact(message)
        if reply != "":
            await message.channel.send(reply)
            answered = True

        reply = check_for_thanks(message)
        if reply != "":
            await message.channel.send(reply)
            answered = True

        reply = check_for_weather(message)
        if reply != "":
            await message.channel.send(reply)
            answered = True

        reply = check_for_music(message)
        if reply != "":
            await message.channel.send(reply)
            answered = True

        reply = check_for_whats_up(message)
        if reply != "":
            await message.channel.send(reply)
            answered = True

        reply = check_for_meme(message)
        if reply != "":
            await message.channel.send(file=discord.File(reply))
            answered = True

        reply = check_for_goodbye(message)
        if reply != "":
            await message.channel.send(reply)
            answered = True

        reply = check_for_time(message)
        if reply != "":
            await message.channel.send(reply)
            answered = True

        if not answered:
            reply = send_google_link(message)
            await message.channel.send(reply)


@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


client.run(TOKEN)
