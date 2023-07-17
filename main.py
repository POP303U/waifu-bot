import discord
from discord.ext import commands
import requests

url = 'https://api.waifu.im/search'

intents = discord.Intents.default()
intents.message_content = True  # Enable the message content intent

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is connected as {bot.user.name}')

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
async def waifu(ctx):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        image_url = data['images'][0]['url']
        await ctx.send(image_url)
    else:
        await ctx.send('Failed to fetch waifu image.')

bot.run('MTEzMDQ5MTY1MjM0NDEzMTYzNQ.G2OFAD.-_7Ojb4woXsj15HtqO_fPtuilBBx-P3LytVYcw')
