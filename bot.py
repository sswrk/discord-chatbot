import os

import discord
from dotenv import load_dotenv

from intents.covid import try_covid
from intents.fun_fact import try_fun_fact
from intents.goodbye import try_goodbye
from intents.google import send_google_link
from intents.hello import try_hello
from intents.mem import try_meme
from intents.music import try_music
from intents.random import try_random
from intents.thanks import try_thanks
from intents.time import try_time
from intents.weather import try_weather
from intents.whats_up import try_whats_up
from intents.who_are_you import try_who_are_you

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
    if message.channel.name == os.getenv('DISCORD_CHANNEL') and not message.author.bot:
        print(message.author.display_name + ": " + message.content)
        message.content = message.content.lower()
        answered = False

        reply = try_hello(message)
        if reply != "":
            await message.channel.send(reply)
            answered = True

        reply = try_who_are_you(message)
        if reply != "":
            await message.channel.send(reply)
            answered = True

        reply = try_fun_fact(message)
        if reply != "":
            await message.channel.send(reply)
            answered = True

        reply = try_thanks(message)
        if reply != "":
            await message.channel.send(reply)
            answered = True

        reply = try_weather(message)
        if reply != "":
            await message.channel.send(reply)
            answered = True

        reply = try_music(message)
        if reply != "":
            await message.channel.send(reply)
            answered = True

        reply = try_whats_up(message)
        if reply != "":
            await message.channel.send(reply)
            answered = True

        reply = try_meme(message)
        if reply != "":
            await message.channel.send(file=discord.File(reply))
            answered = True

        reply = try_goodbye(message)
        if reply != "":
            await message.channel.send(reply)
            answered = True

        reply = try_time(message)
        if reply != "":
            await message.channel.send(reply)
            answered = True

        reply = try_covid(message)
        if reply != "":
            await message.channel.send(reply)
            answered = True

        reply = try_random(message)
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
