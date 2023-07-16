import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()
# intents
intents = discord.Intents.default()
intents.message_content = True

# bot setup
bot = commands.Bot(command_prefix=".", intents=intents,
                   status=discord.Status.online, activity=discord.Game(name=" with your mother"))


@bot.event
async def on_ready():
    print("Successfully logged in!")


@bot.command()
async def voice(ctx):
    await ctx.author.voice.channel.connect()
    voice = ctx.voice_client
    ctx.voice_client.play(discord.FFmpegPCMAudio(
        "assets/babi.mp3"))


@bot.command()
async def leave(ctx):
    channel = ctx.voice_client
    if (not channel):
        return await ctx.reply("I'll break ya fucking legs! You Fucking donut!")
    else:
        await channel.disconnect()

bot.run(token=os.getenv("DISCORD_BOT_TOKEN"))
