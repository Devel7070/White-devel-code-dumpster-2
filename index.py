import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()
<<<<<<< HEAD
#intents
=======
# intents
>>>>>>> e4f1a03469f71c0efc2ad401e7abea0e4f293fff
intents = discord.Intents.default()
intents.message_content = True

# bot setup
bot = commands.Bot(command_prefix=".", intents=intents,
                   status=discord.Status.online, activity=discord.Game(name=" with your mother"))


@bot.event
async def on_ready():
    print("Successfully logged in!")


@bot.command()
async def ping(ctx):
    while True:
        await ctx.reply("I hate niggers!")
        asyncio.sleep(2)

bot.run(token=os.getenv("DISCORD_BOT_TOKEN"))
