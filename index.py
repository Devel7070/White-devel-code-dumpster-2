import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

#intents
intents = discord.Intents.default()
intents.message_content = True

# bot setup
bot = commands.Bot(command_prefix=".", intents = intents, status = discord.Status.idle, activity = discord.Game(name = " with your"))

@bot.event
async def on_ready():
    print("Successfully logged in!")
    
@bot.command()
async def ping(ctx):
    await ctx.send("I hate niggers")

bot.run(token=os.getEnv("DISCORD_BOT_TOKEN"))