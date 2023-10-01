import discord
from discord.ext import commands
from bot_logic import gen_pass
from bot_logic import invert
from random import choice
from bot_logic import get_duck_image_url
import nacl
import youtube_dl
import os
import requests 
from random import choice



password_help = '!password (lenght)'
hello_help = '!hello'
bye_help = '!bye'
heh_help = '!heh (lenght)'
inv_help = '!inv (text)'
print(os.listdir('images'))

file_path = "deutch.mp3"
full_path = os.path.abspath(file_path)
print(full_path)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')
    
@bot.command()
async def password(ctx, pass_lenght = 10):
    await ctx.send(gen_pass(pass_lenght))
    
@bot.command() 
async def bye(ctx):
    await ctx.send(f'Пока {client.user}!')
    
@bot.command() 
async def inv(ctx, text):
    await ctx.send(invert(text))

@bot.command() 
async def mem(ctx):
    with open('images/mem1.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    
@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def ran_mem(ctx):
    ran_mem = choice(os.listdir('images'))
    with open(f'images/{ran_mem}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture) 
           
@bot.command()
async def help_mes(ctx):
    help_text = f"{password_help}\n{hello_help}\n{bye_help}\n{heh_help}\n{inv_help}"
    await ctx.send(help_text)
    
@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)
    
    
    
    
    
    
    
@bot.command()
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
    
@bot.command()
async def leave(ctx):
    await ctx.voice_client.disconnect()
    
    
    
@bot.command()
async def play(ctx, file_path = full_path):
    if not ctx.voice_client:
        await ctx.invoke(join)

    source = discord.FFmpegPCMAudio(file_path)
    ctx.voice_client.play(source)
    
@bot.command()
async def pause(ctx):
    ctx.voice_client.pause()
    
@bot.command()
async def resume(ctx):
    ctx.voice_client.resume()
    
@bot.command()
async def stop(ctx):
    ctx.voice_client.stop()

bot.run("token")







