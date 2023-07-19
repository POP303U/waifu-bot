import discord 
from discord.ext import commands, tasks
import time
import requests

waifu_url = 'https://waifu.pics/api/'
dog_url = 'https://dog.ceo/api/breeds/image/random'
cat_url = 'https://api.thecatapi.com/v1/images/search'
duck_url = 'https://random-d.uk/api/v2'

intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'#------------------------------#')
    print(f'|   waifu-bot [version 1.0]    |')
    print(f'| Activity: {bot.activity}               |')
    print(f'| Status: {bot.status}               |')
    print(f'| Bot is connected as {bot.user.name}    |')
    print(f'#-------------------------------#')
    print(f'Console:')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  #Ignore messages sent by the bot itself

    if 'lmao' in message.content.lower():
        await message.channel.send('not funny')

    await bot.process_commands(message)

@bot.command()
async def dog(ctx):
    response = requests.get(dog_url)
    data = response.json()
    if data['status'] == 'success':
        image_url = data['message']
        await ctx.send(image_url)
    else:
        await ctx.send('Failed to fetch dog image.')

@bot.command()
async def dog_repeat(ctx, arg1):
    count = 0
    try:
        limit = int(arg1)
    except:
        print("Failed to convert arg1 to int")
    while True:
        if count == limit:
            break
        count = count + 1
        response = requests.get(dog_url)
        data = response.json()
        if data['status'] == 'success':
            image_url = data['message']
            await ctx.send(image_url)
            print(f'Log: sent image: {image_url}, count: {count}')
            time.sleep(1)
        else:
            await ctx.send('Failed to fetch dog image.')


@bot.command()
async def cat(ctx):
    response = requests.get(cat_url)
    data = response.json()
    if response.status_code == 200:
        image_url = data[0]['url']
        print(image_url)
        await ctx.send(image_url)
    else:
        await ctx.send('Failed to fetch cat image.')

@bot.command()
async def cat_repeat(ctx, arg1):
    count = 0
    try:
        limit = int(arg1)
    except:
        print("Failed to convert arg1 to int")
    while True:
        if count == limit:
            break
        count = count + 1
        response = requests.get(cat_url)
        data = response.json()
        if response.status_code == 200:
            image_url = data[0]['url']
            await ctx.send(image_url)
            print(f'Log: sent image: {image_url}, count: {count}')
            time.sleep(1)
        else:
            await ctx.send('Failed to fetch cat image.')

@bot.command()
async def waifu_repeat(ctx, arg1="sfw", arg2="waifu", arg3="5"):
    count = 0
    try:
        limit = int(arg3)
    except:
        print("Failed to convert arg3 to int")
    print("Loop:")
    while True:
        if count == limit:
            break
        count = count + 1
        response = requests.get(waifu_url + arg1 + '/' + arg2)
        if response.status_code == 200:
            data = response.json()
            image_url = data['url']
            await ctx.send(image_url)
            print(f'Log: sent image: {image_url}, count: {count}')
            time.sleep(1)
        else:
            await ctx.send('Failed to fetch waifu image.')
    print("Loop finished.")

@bot.command()
async def waifu(ctx, arg1="sfw", arg2="waifu"):
    response = requests.get(waifu_url + arg1 + '/' + arg2)
    if response.status_code == 200:
        data = response.json()
        image_url = data['url']
        await ctx.send(image_url)
        print(f'Log: sent image: {image_url}')
    else:
        await ctx.send('Failed to fetch waifu image.')

@bot.command()
async def duck_repeat(ctx, arg1):
    count = 0
    try:
        limit = int(arg1)
    except:
        print("Failed to convert arg1 to int")
    print("Loop:")
    while True:
        if count == limit:
            break
        count = count + 1
        response = requests.get(duck_url, '/random')
        if response.status_code == 200:
            data = response.json()
            print(data)
            image_url = data['url']
            await ctx.send(image_url)
            print(f'Log: sent image: {image_url}, count: {count}')
            time.sleep(1)
        else:
            await ctx.send('Failed to fetch duck image.')
    print("Loop finished.")

@bot.command()
async def duck(ctx):
    response = requests.get(duck_url, '/random')
    if response.status_code == 200:
        data = response.json()
        image_url = data['url']
        await ctx.send(image_url)
        print(f'Log: sent image: {image_url}')
    else:
        await ctx.send('Failed to fetch duck image.')

bot.run('')