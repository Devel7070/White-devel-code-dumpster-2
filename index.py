import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import asyncio
import random
import time

load_dotenv()
# intents
intents = discord.Intents.default()
intents.message_content = True

# bot setup
bot = commands.Bot(
    command_prefix=".",
    intents=intents,
    status=discord.Status.online,
    activity=discord.Game(name=" with your mother"),
)


@bot.event
async def on_ready():
    print("Successfully logged in!")


@bot.event
async def on_message(msg):
    if ("nigga" in msg.content.lower()) or ("nigger" in msg.content.lower()):
        await msg.reply(
            "NUH UH! You are not black you can't say that. I am and I will say it. NI-")
    await bot.process_commands(msg)


@bot.command()
async def voice(ctx):
    await ctx.author.voice.channel.connect()
    voice = ctx.voice_client
    ctx.voice_client.play(discord.FFmpegPCMAudio("assets/babi.mp3"))


@bot.command()
async def leave(ctx):
    channel = ctx.voice_client
    if not channel:
        return await ctx.reply("I'll break ya fucking legs! You Fucking donut!")
    else:
        await channel.disconnect()


options = ("r", "p", "s")


async def play_vc(ctx, path):
    author = ctx.author.voice
    voice = ctx.voice_client
    if author:
        if voice:
            if voice.is_playing():
                voice.stop()
            if voice.channel.id != author.channel.id:
                await voice.disconnect()
                await author.channel.connect()
        else:
            await author.channel.connect()
    else:
        return

    ctx.voice_client.play(discord.FFmpegPCMAudio(path))


@bot.command()
async def rps(ctx, arg):
    if arg.lower()[0] not in options:
        return await ctx.reply(
            "Give argument in form of rock, paper or scissor (r, p, or s)"
        )
    user_choice = arg.lower()[0]
    bot_choice = random.choice(options)

    await ctx.reply(f"I choose {format(bot_choice)}")
    voice = ctx.author.voice
    if bot_choice == user_choice:
        await ctx.reply("Ok")
        await play_vc(ctx, "assets/babi.mp3")

    elif (
        (bot_choice == "r" and user_choice == "p")
        or (bot_choice == "p" and user_choice == "s")
        or (bot_choice == "s" and user_choice == "r")
    ):
        await ctx.reply("You win! You suck anyways!")
        await play_vc(ctx, "assets/GALSCREAMING.mp3")

    else:
        await ctx.reply("I win!")


def format(choice):
    if choice == "r":
        return "Rock"
    if choice == "p":
        return "Paper"
    if choice == "s":
        return "Scissors"


bot.run(token=os.getenv("DISCORD_BOT_TOKEN"))
