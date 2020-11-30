import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

bot = commands.Bot(command_prefix='>', description="Este es un bot de prueba")


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def sum(ctx, num1: int, num2: int):
    await ctx.send(num1 + num2)


@bot.command()
async def saludar(ctx, nombre: str):
    await ctx.send("Hola " + nombre + " si ya despertaste!")


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="Dota2", url="http://twitch.tv/accountname"))
    print('Mi bot esta listo')


bot.run(os.getenv('DISCORD_TOKEN'))