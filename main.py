import discord
import time
from discord.ext import commands
import requests

url = 'https://api.waifu.im/search'

intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'#------------------------------#')
    print(f'| Activity: {bot.activity}               |')
    print(f'| Status: {bot.status}               |')
    print(f'| Bot is connected as {bot.user.name}    |')
    print(f'#------------------------------#')
    print(f'Console:')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # Ignore messages sent by the bot itself

    if 'lmao' in message.content.lower():
        await message.channel.send('not funny')

    if 'what' in message.content.lower():
        await message.channel.send('negawatt')

    await bot.process_commands(message)

@bot.command()
async def die(ctx):
    await ctx.send('you should kys')

@bot.command()
async def waifu_repeat(ctx, arg1):
    count = 0
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            image_url = data['images'][0]['url']
            time.sleep(int(arg1))
            await ctx.send(image_url)
            print(f'Log: sent image: {image_url}, count: {count}, delay {arg1}')
            count = count + 1
        else:
            await ctx.send('Failed to fetch waifu image.')

@bot.command()
async def waifu(ctx):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        image_url = data['images'][0]['url']
        await ctx.send(image_url)
        print(f'Log: sent image: {image_url}')
    else:
        await ctx.send('Failed to fetch waifu image.')

bot.run('')