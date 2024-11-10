import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık.')

@bot.command()
async def secret_function(ctx, a = 5, b = 8):
    await ctx.send(a + b)



bot.run("token")
