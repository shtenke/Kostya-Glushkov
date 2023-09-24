import discord
from discord.ext import commands
from bot_logic import gen_pass
from bot_logic import invert
from random import choice

password_help = '!password (lenght)'
hello_help = '!hello'
bye_help = '!bye'
heh_help = '!heh (lenght)'
inv_help = '!inv (text)'
    
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
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def help_mes(ctx):
    help_text = f"{password_help}\n{hello_help}\n{bye_help}\n{heh_help}\n{inv_help}"
    await ctx.send(help_text)

bot.run("MTE1Mjg5OTk1Nzk3Njc0ODE1Mg.GzqEln.AVfgbVm_MevRiqFnPOalKRhtfQOEpb7-QVZUrc")







