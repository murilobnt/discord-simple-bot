import discord
from discord.ext import commands

class SimpleCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def say_hi(self, ctx):
        await ctx.send("Hi!")
