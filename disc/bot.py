import discord
from discord.ext import commands
from model.llm import chain_retriever
from threading import Thread

# setup intents
intents = discord.Intents.default()
intents.message_content = True

# setup bot command
bot = commands.Bot(command_prefix="/", intents=intents)


# event to check the bot it ready
@bot.event
async def on_ready():
    print(f"Bot is ready as {bot.user.name}")


# command to ask the bot questions
@bot.command(name="ask")
async def ask(ctx, *, message):
    await ctx.send('gathering response...')

    response = chain_retriever(message)

    await ctx.send(response)






