import discord
from discord.ext import commands
import os

from src.cogs.simple_cog import SimpleCog

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

bot.add_cog(SimpleCog(bot))
bot.run(os.environ['DISCORD_BOT_KEY'])
