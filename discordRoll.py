import discord
from discord.ext import commands
import random

bot = commands.Bot(command_prefix='!')

@bot.command()
async def roll(ctx, number):
  try:
    arg = random.randint(1, int(number))
  except ValueError:
    await ctx.send("What the fuck is that???")
  else:
    await ctx.send(str(arg))
    
bot.run('TOKEN')
