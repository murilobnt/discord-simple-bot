import discord
from discord.ext import commands

from datetime import datetime

class SimpleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def say_hi(self, ctx):
        await ctx.send("Hi!")

    @commands.command(pass_context=True)
    async def say_datetime(self, ctx):
        await ctx.send(str(datetime.now()))
