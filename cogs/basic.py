from twitchio.ext import commands
import os
import json


class basic(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot


    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f"Hello, {ctx.author.name}!")

    @commands.Cog.event()
    async def event_message(self, message):
        if message.echo:
            return
        print(message.content)

    @commands.command()
    async def botuptime(self, ctx: commands.Context):
        """Tells you how long the bot has been up for."""
        try:
            await ctx.send(f"Bot uptime: {self.bot.get_uptime(which=self.bot.bot_uptime)}!")
        except Exception as e:
            print(e)
    
    # @commands.command()
    # async def uptime(self, ctx: commands.Context):
    #     """Tells you how long the streamer has been up for."""
    #     try:
    #         await ctx.send(f"Uptime: {self.bot.get_uptime(which=self.bot.uptime)}!")
    #     except Exception as e:
    #         print(e)
        
    


def prepare(bot: commands.Bot):
    bot.add_cog(basic(bot))